from django.db import models


class Skill(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    psychic = models.BooleanField(default=False)

    def __str__(self):
        return self.name

