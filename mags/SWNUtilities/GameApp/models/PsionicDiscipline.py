from django.db import models


class PsionicDiscipline(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)


class PsionicDisciplineLevel(models.Model):
    discipline = models.ForeignKey(
        'PsionicDiscipline',
        on_delete=models.CASCADE,
    )
    character = models.ForeignKey(
        'Character',
        on_delete=models.CASCADE
    )
    level = models.PositiveSmallIntegerField(
        default=0,
    )
