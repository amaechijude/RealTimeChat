from channels.generic.websocket import WebsocketConsumer
from django.shortcuts import get_object_or_404
from .models import Room, RoomChat
import json
from django.template.loader import render_to_string

class ChatRoomConsumer(WebsocketConsumer):
    #connect method
    def connect(self):
        #user object
        self.user = self.scope['user']
        #room name from the url
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        #chat room instance
        self.chatroom = get_object_or_404(Room, group_name=self.room_name)
        self.accept()


    #recieving messages. receives the messages as textdata
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        content = text_data_json['content']
        author = self.user.profile
        room = self.chatroom
        new_chat = RoomChat.objects.create(room=room,
                                           author=author,
                                           content=content)

