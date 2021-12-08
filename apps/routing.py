from django.urls import path
from apps import consumers

websocket_urlpatterns = [
    # url(r'^ws/msg/(?P<room_name>[^/]+)/$', consumers.SyncConsumer),
    path("", consumers.ChatConsumer.as_asgi()),
]