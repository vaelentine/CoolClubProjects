from django.db import models


class PsionicTechnique(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    level = models.PositiveSmallIntegerField(default=1)
    discipline = models.ForeignKey(
        'PsionicDiscipline',
        on_delete=models.CASCADE,
    )
