from django.db import models
from django import template

register = template.Library()


class Background(models.Model):
    name = models.CharField(max_length=100, unique=True, null=True)
    heading = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.name)

