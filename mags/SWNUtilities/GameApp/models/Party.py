from django.db import models


class Party(models.Model):
    name = models.CharField(max_length=100, null=True, unique=True)
    # TODO: location = models.ForeignKey('Location', on_delete=models.SET_NULL)

    def __str__(self):
        return self.name
