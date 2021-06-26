from django.db import models


class Attributes(models.Model):
    strength = models.PositiveSmallIntegerField(default=10)
    dexterity = models.PositiveSmallIntegerField(default=10)
    constitution = models.PositiveSmallIntegerField(default=10)
    intelligence = models.PositiveSmallIntegerField(default=10)
    wisdom = models.PositiveSmallIntegerField(default=10)
    charisma = models.PositiveSmallIntegerField(default=10)
    hit_point_max = models.PositiveSmallIntegerField(default=10)
    current_hit_points = models.SmallIntegerField(default=10)

    def __str__(self):
        return str([
            self.strength,
            self.dexterity,
            self.constitution,
            self.intelligence,
            self.wisdom,
            self.charisma,
            self.hit_point_max
                ])
