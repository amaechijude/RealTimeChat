import json

from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Room, RoomChat
from channels.db import database_sync_to_async
from channels.layers import get_channel_layer


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope['user']
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.chatroom = await self.get_room(self.room_name)
    
        await self.channel_layer.group_add(
            self.room_name, self.channel_name
        )

        await self.accept()

    # disconnect
    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_name, self.channel_name
        )


    #receive method
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        self.content = text_data_json['content']
        self.username = text_data_json['author']

        new_chat_json = {
            "content": self.content,
            "author": self.username,
            "online_count": 1,#to be updatedf

        }
        #save to dastatbase
        await self.save_chat_to_db()

        #stream chats to room members
        channel_layer = get_channel_layer()
        await channel_layer.group_send(
            self.room_name,
            {
                "type": "chat_message",
                "message": new_chat_json
            }
        )
        
    #meesage event
    async def chat_message(self, event):
        message = event["message"]

        #Send message to websocket
        await self.send(text_data=json.dumps(message))
    

    # save chat to database
    @database_sync_to_async
    def save_chat_to_db(self):
        chat = self.content
        author = self.user.profile
        room = self.chatroom
        new_chat = RoomChat.objects.create(room=room,author=author,content=chat)
        new_chat.save()
        #return new_chat

    @database_sync_to_async
    def get_room(self, room_name):
        return Room.objects.get(room_name=room_name)
