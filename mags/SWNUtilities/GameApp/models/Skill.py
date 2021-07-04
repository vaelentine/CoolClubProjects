from django.db import models

class Skill(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        null=True)
    description = models.CharField(
        max_length=1000,
        null=True,
        blank=True
    )