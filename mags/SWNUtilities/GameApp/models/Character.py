from django.db import models
from django.urls import reverse

class Character(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        null=True)
    player = models.ForeignKey(
        'Player',
        related_name='character_players',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    attributes = models.OneToOneField(
        'Attributes',
        null=True,
        blank=True,
        related_name='character_attributes',
        on_delete=models.CASCADE
    )
    faction = models.ForeignKey(
        'Faction',
        null=True,
        blank=True,
        related_name='character_factions',
        on_delete=models.SET_NULL
    )
    party = models.ForeignKey(
        'Party',
        null=True,
        blank=True,
        related_name='character_party',
        on_delete=models.SET_NULL)
    pronouns = models.ForeignKey(
        'Pronouns',
        null=True,
        blank=True,
        related_name='character_pronouns',
        on_delete=models.SET_NULL
    )
    background = models.ForeignKey(
        'Background',
        null=True,
        blank=True,
        related_name='character_backgrounds',
        on_delete=models.SET_NULL
    )
    # character_class = models.ForeignKey(
    #     'CharacterClass',
    #     null=True,
    #     blank=True,
    #     related_name='character_classes',
    #     on_delete=models.SET_NULL
    # )

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('character_detail', kwargs={'pk': self.pk})