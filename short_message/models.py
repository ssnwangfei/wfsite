from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Message(models.Model):
    """
    用户发送的消息
    """
    user_from = models.ForeignKey(User, on_delete=models.CASCADE, related_name="users_from")
    user_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name="users_to")
    tag = models.CharField('app tag', max_length=10)
    message = models.CharField(max_length=1000)
    date = models.DateTimeField('date created')
