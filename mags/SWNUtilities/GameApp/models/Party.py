from django.db import models


class Party(models.Model):
    name = models.CharField(max_length=100, null=True)
    # TODO: location = models.ForeignKey('Location', on_delete=models.SET_NULL)
