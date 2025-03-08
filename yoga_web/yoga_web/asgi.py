import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
from pose_checker import consumers

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'yoga_web.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(), 
    "websocket": AuthMiddlewareStack(
        URLRouter([
            path("ws/yoga/", consumers.YogaConsumer.as_asgi()), 
        ])
    ),
})
