from django.db import models

# Create your models here.

class User(models.Model):
    id = models.IntegerField(primary_key=True, unique = True)
    name = models.CharField(max_length=30, unique = True)
    desc = models.CharField(max_length=100)
    create_date = models.DateTimeField('date created')


class message(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=1000)
    tag = models.CharField(max_length=10)
    send_date = models.DateTimeField('date created')
    recv_count = models.IntegerField(default=0)