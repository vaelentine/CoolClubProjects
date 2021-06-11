from django.db import models


class Background(models.Model):
    name = models.CharField(max_length=100)
    header = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name
