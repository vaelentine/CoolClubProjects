from django.db import models


class Focus(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    level_1 = models.TextField()
    level_2 = models.TextField()
