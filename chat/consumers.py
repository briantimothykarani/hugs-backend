'''import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_group_name = "chat_room"

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()
        self.send(text_data=json.dumps({
            'type': 'chat',
            'message': '🔗 Connected to chat.'
        }))

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def receive(self, text_data):
        try:
            text_data_json = json.loads(text_data)
            message = text_data_json.get('message', '')

            if message.strip():
                async_to_sync(self.channel_layer.group_send)(
                    self.room_group_name,
                    {
                        'type': 'chat_message',
                        'message': message
                    }
                )
        except json.JSONDecodeError:
            self.send(text_data=json.dumps({
                'type': 'error',
                'message': 'Invalid JSON'
            }))

    def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'type': 'chat',
            'message': message
        })) '''
import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        # Expect URL to be /ws/chat/<room_name>/
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f"chat_{self.room_name}"

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()
        self.send(text_data=json.dumps({
            'type': 'chat',
            'message': '🔗 Connected to chat.',
            'sender': 'system'
        }))

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def receive(self, text_data):
        try:
            text_data_json = json.loads(text_data)
            message = text_data_json.get('message', '')
            sender = text_data_json.get('sender', 'anonymous')

            if message.strip():
                async_to_sync(self.channel_layer.group_send)(
                    self.room_group_name,
                    {
                        'type': 'chat_message',
                        'message': message,
                        'sender': sender,
                    }
                )
        except json.JSONDecodeError:
            self.send(text_data=json.dumps({
                'type': 'error',
                'message': 'Invalid JSON'
            }))

    def chat_message(self, event):
        message = event['message']
        sender = event.get('sender', 'anonymous')

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'type': 'chat',
            'message': message,
            'sender': sender,
        }))

