from channels.generic.websocket import WebsocketConsumer


class ChatRoomConsumer(WebsocketConsumer):
    def connect(self):
        self.user = self.scope['user']
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.accept()