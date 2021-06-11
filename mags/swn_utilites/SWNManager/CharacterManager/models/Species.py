from django.db import models


class Species(models.Model):
    name = models.CharField(max_length=100)
    header = models.CharField(max_length=200)
    description = models.TextField()
