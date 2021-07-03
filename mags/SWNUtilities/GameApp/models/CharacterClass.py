from django.db import models


class CharacterClass(models.Model):
    name = models.CharField(max_length=100, unique=True, null=True)
    heading = models.TextField(max_length=200, null=True)
    description = models.TextField(null=True)

    def __str__(self):
        return str(self.name)
