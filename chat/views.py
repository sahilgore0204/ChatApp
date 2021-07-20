from django.shortcuts import render
from .models import ChatModel
# Create your views here.
from django.http import HttpResponse 
def index(req):
    return render(req,'chat/index.html')
def roomview(req):
    room_no=req.POST['room_no']
    name=req.POST['name']
    messages=[]
    for x in ChatModel.objects.filter(room_no=room_no):
        messages.append(x)
    return render(req,'chat/room.html',{
        'room_no':room_no,
        'name':name,
        'messages':messages
    })