from .consumer import ChatConsumer
from django.urls import re_path


websocket_urlpatterns = [
        re_path('ws/notification/<str:room_name>/', ChatConsumer.as_asgi()),

        ]
