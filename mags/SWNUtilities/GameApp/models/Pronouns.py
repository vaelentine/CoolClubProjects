from django.db import models


class Pronouns(models.Model):
    gender_name = models.CharField(max_length=50, default='non-binary')
    subject_pronoun = models.CharField(max_length=10, default='they')
    object_pronoun = models.CharField(max_length=10, default='them')
    possessive_adj = models.CharField(max_length=10, default='their')
    possessive_pronoun = models.CharField(max_length=10, default='theirs')
    reflexive_pronoun = models.CharField(max_length=10, default='themself')

    def __str__(self):
        return f'{self.gender_name}: {self.subject_pronoun}/{self.object_pronoun}/{self.possessive_adj}'
