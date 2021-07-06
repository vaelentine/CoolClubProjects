from django.db import models


class Skill(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        null=True)
    description = models.CharField(
        max_length=1000,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name


class SkillLevel(models.Model):
    COMPETENT = 0
    EXPERIENCED = 1
    EXPERT = 2
    MASTER = 3
    SUPERLATIVE = 4
    LEVEL_CHOICES = (
        (COMPETENT, 'basic competency'),
        (EXPERIENCED, 'experienced professional'),
        (EXPERT, 'respected veteran expert'),
        (MASTER, 'mastery, best on the planet'),
        (SUPERLATIVE, 'superlative expertise, best in the sector')
    )
    skill = models.ForeignKey(
        'Skill',
        on_delete=models.CASCADE,
    )
    level = models.PositiveSmallIntegerField(choices=LEVEL_CHOICES, default=COMPETENT)
    character = models.ForeignKey(
        'Character',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return "{}_{}".format(self.skill.__str__(), self.level.__str__())
