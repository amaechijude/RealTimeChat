from .consumer import ChatRoomConsumer, ChatConsumer
from django.urls import re_path, path


websocket_urlpatterns = [
        # path("ws/chat/<room_name>", ChatRoomConsumer.as_asgi()),
        path("ws/chat/<room_name>", ChatConsumer.as_asgi()),
        ]
