import json
from channels.generic.websocket import AsyncJsonWebsocketConsumer

class ChatConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add('chat', self.channel_name)

        await self.accept()

        self.user = str.split(self.channel_name, '!')[1]
        await self.send_json({
            'type': 'chat.connect',
            'event': self.user
        })

        await self.channel_layer.group_send('chat', {
            'type': 'chat_broadcast',
            'event': {
                'type': 'chat.connect.new',
                'event': {
                    'user': self.user,
                }
            }
        })

    async def disconnect(self, close_code):
        await self.channel_layer.group_send('chat', {
            'type': 'chat_broadcast',
            'event': {
                'type': 'chat.connect.disconnect',
                'event': {
                    'user': self.user,
                }
            }
        })

        await self.close(close_code)
        await self.channel_layer.group_discard('chat', self.channel_name)

    async def receive(self, text_data):
        text_data = json.loads(text_data)
        if text_data['type'] == 'chat.message':
            await self.send_json({
                'type': 'chat.message.me',
                'event': {
                    'message': text_data['event']
                }
            })

            await self.channel_layer.group_send('chat', {
               'type': 'chat_broadcast',
               'event': {
                    'type': 'chat.message.others',
                    'event': {
                         'user': self.user,
                         'message': text_data['event'],
                    }
               }
            })

    async def chat_broadcast(self, event):
        await self.send_json(event['event'])