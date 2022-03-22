from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserProfile(models.Model):
    """
    用户附加信息
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(max_length=20, unique=True, blank=False)
    desc = models.CharField("User Description", max_length=100)
    telephone = models.CharField("Telephone", max_length=50, blank=True)

    def __str__(self):
        return "{}".format(self.user.__str__())


class UserRelationship(models.Model):
    """
    用户关系
    """
    user_me = models.ForeignKey(User, on_delete=models.CASCADE, related_name='me_relationships')
    user_you = models.ForeignKey(User, on_delete=models.CASCADE, related_name='to_me_relationships')
    relation = models.CharField("Relationship", max_length=10, blank=False)
