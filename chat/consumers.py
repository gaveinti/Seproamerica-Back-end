import json
from channels.generic.websocket import AsyncWebsocketConsumer


class chatConsumers(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        print("Nuevo usuario conectado")

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
        print("usuario desconectado")

    async def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        #name = text_data_json['name']
        print(message)
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'message_confirm',
                'message': message,
                # 'name':name
            }
        )

    async def message_confirm(self, event):
        message = event['message']
        #name = event['name']

        await self.send(text_data=json.dumps({
            'message': message,
            # 'name':name
        }))

    async def chat_message(self, event):
        message = event['message']
        #name = event['name']

        await self.send(text_data=json.dumps({
            'message': message,
            # 'name':name
        }))
