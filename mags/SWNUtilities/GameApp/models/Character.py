from django.db import models
from .Player import Player


class Character(models.Model):
    name = models.CharField(max_length=100, unique=True)
    player = models.ForeignKey('Player', related_name='character_players', null=True, on_delete=models.SET_NULL)
    attributes = models.ForeignKey('Attributes', null=True, related_name='character_attributes', on_delete=models.SET_NULL)
    faction = models.ForeignKey('Faction', null=True, related_name='character_factions', on_delete=models.SET_NULL)
    party = models.ForeignKey('Party', null=True, related_name='character_party', on_delete=models.SET_NULL)

    def __str__(self):
        return str(self.name)

