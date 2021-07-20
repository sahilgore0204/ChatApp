from django.db import models
class ChatModel(models.Model):
    room_no=models.IntegerField()
    message=models.TextField()
    def __str__(self):
        return self.message
# Create your models here.
