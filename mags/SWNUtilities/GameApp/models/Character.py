from django.db import models
from .Player import Player


class Character(models.Model):
    name = models.CharField(max_length=100, unique=True)
    player = models.ForeignKey('Player', related_name='characters', null=True, on_delete=models.SET_NULL)
    attributes = models.ForeignKey('Attributes', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return str(self.name)
