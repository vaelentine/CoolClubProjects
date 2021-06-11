from django.db import models


class CharClass(models.Model):
    name = models.CharField(max_length=100)
    ability = models.ManyToManyField('ClassAbility', related_name='charclasses')

    def __str__(self):
        return self.name

