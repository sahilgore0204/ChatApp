from django.urls import path
from . import consumers
weburl_patterns=[
    path('ws/chat/<int:room_no>/',consumers.ChatConsumer.as_asgi()),
]