from channels.routing import ProtocolTypeRouter, URLRouter
import os
from channels.auth import AuthMiddlewareStack
import apps.routing
from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "websocket_demo.settings")
django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter({
    'http': django_asgi_app,
    'websocket': AuthMiddlewareStack(
        URLRouter(
            apps.routing.websocket_urlpatterns
        )
    )
})