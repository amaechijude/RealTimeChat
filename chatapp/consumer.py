import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import Room, Message


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = f"room_{self.scope['url_route']['kwargs']['room_name']}"
        await self.channel_layer.group_add(self.room_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_name, self.channel_name)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        content = text_data_json

    async def send_content(self, event):
        data = event['content']
        await self.create_content(data=data)
        response_data = {
                'author': data['author'],
                'content': data['content']
                }
        await self.send(text_data=json.dumps({'content': response_data}))

    @database_sync_to_async
    def create_content(self, data):
        get_room_by_name = Room.objects.get(room_name=data['room_name'])
        if not Message.objects.filter(content=data['content']).exists():
            new_content = Message(room=get_room_by_name, author=data['author'], content=data['content'])
            new_content.save()
