from channels.generic.websocket import AsyncWebsocketConsumer
import json
from .models import ChatModel
from asgiref.sync import sync_to_async
class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name=self.scope['url_route']['kwargs']['room_no']
        self.room_group_name='chat_'+str(self.room_name)
        await self.channel_layer.group_add(self.room_group_name,self.channel_name)
        await self.accept()
    async def disconnect(self):
        await self.channel_layer.group_discard(self.room_group_name,self.channel_name)
    async  def receive(self, text_data):
        data=json.loads(text_data)
        msg=data['msg']
        await sync_to_async(ChatModel(room_no=self.room_name,message=msg).save)()
        await self.channel_layer.group_send(self.room_group_name,{
            'msg':msg,
            'type':'send_back'
        })
    async def send_back(self,e):
        msg=e['msg']
        await self.send(text_data=json.dumps({
            'msg':msg
        }))
   

