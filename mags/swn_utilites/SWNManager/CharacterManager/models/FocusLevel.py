from django.db import models


class FocusLevel(models.Model):
    level1 = 1
    Level2 = 2

    focus = models.ForeignKey('Focus', on_delete=models.SET_NULL, null=True)
    character = models.ForeignKey('Character', on_delete=models.SET_NULL, null=True)
