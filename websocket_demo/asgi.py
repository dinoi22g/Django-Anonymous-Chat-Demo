"""
ASGI config for websocket_demo project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

import websocket_demo.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'websocket_demo.settings')

application = websocket_demo.routing.application
