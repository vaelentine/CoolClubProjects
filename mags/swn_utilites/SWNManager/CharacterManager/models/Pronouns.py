from django.db import models


class Pronouns(models.Model):
    gender_name = models.CharField(max_length=50, null=True)
    subject_pronoun = models.CharField(max_length=10)
    object_pronoun = models.CharField(max_length=10)
    possessive_adj = models.CharField(max_length=10)
    possessive_pronoun = models.CharField(max_length=10)
    reflexive_pronoun = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.gender_name}: {self.subject_pronoun}/{self.object_pronoun}/{self.possessive_adj}'
