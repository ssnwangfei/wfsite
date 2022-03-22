from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class AppTag(models.Model):
    name = models.CharField("Application Tag", max_length=10, blank=False)

    def __str__(self):
        return "{}".format(self.name)


class Message(models.Model):
    """
    用户发送的消息
    """
    user_from = models.ForeignKey(User, on_delete=models.CASCADE, related_name="messages_from")
    user_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name="messages_to")
    tag = models.ForeignKey(AppTag, on_delete=models.CASCADE, related_name="messages_tag")
    message = models.CharField(max_length=1000)
    date = models.DateTimeField('date created')

    def __str__(self):
        return "{}".format(self.message)


