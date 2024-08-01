from .consumer import ChatConsumer
from django.urls import path


websocket_urlpatterns = [
        path("ws/chat/<room_name>", ChatConsumer.as_asgi()),
        
        ]
