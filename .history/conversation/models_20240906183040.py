from django.db import models

from item.models import Item
# Create your models here.

class Conversation(models.Model):
    item = models.ForeignKey(Item, related_name='conversations', on_delete=models.CASCADE)
    members = models.M


