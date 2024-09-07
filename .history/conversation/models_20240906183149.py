from django.db import models
from django.contrib.auth.models import User

from item.models import Item
# Create your models here.

class Conversation(models.Model):
    item = models.ForeignKey(Item, related_name='conversations', on_delete=models.CASCADE)
    members = models.ManyToManyField(User, related_name='conversations', models.OneToOneField("app.Model", verbose_name=_(""), on_delete=models.CASCADE))


