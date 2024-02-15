import json
from channels.generic.websocket import AsyncWebsocketConsumer
from rest_framework.permissions import IsAuthenticated

class testConsumer(AsyncWebsocketConsumer):
    #permission_classes = [IsAuthenticated]

    async def connect(self):
        #if not self.scope["user"].is_authenticated:
            #await self.close()

        await self.channel_layer.group_add("notifications", self.channel_name)
        await self.accept()
        await self.send(text_data=json.dumps({'message': '¡Conexión exitosa!'}))

    async def disconnect(self, close_code):
        print(close_code)
        await self.send(text_data=json.dumps({'message': close_code}))

    async def receive(self, text_data=None, bytes_data=None):

        text_data_json = json.loads(text_data)

        await self.channel_layer.group_send(
            "notifications",
            {
                "type": "send_notification",
                "message": text_data_json["message"]
            }
        )

    async def send_notification(self, event):
        message = event['message']
        await self.send(text_data=json.dumps({'message': message}))
