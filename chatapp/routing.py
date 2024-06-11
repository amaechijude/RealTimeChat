from .consumer import ChatConsumer
from django.urls import path


websocket_urlpatterns = [
        path('ws/notification/<str:room_name>/', ChatConsumer.asgi()),

        ]
