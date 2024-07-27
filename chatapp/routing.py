from .consumer import ChatRoomConsumer
from django.urls import re_path, path


websocket_urlpatterns = [
        # re_path('ws/notification/<str:room_name>/', ChatConsumer.as_asgi()),
        path("ws/chat/<room_name>", ChatRoomConsumer.as_asgi()),

        ]
