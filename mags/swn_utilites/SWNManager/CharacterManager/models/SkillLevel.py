from django.db import models


class SkillLevel(models.Model):
    NOVICE = 0
    COMPETENT = 1
    VETERAN = 2
    MASTER = 3
    ELITE = 4
    LEVEL_CHOICES = (
        (NOVICE, 'Novice'),
        (COMPETENT, 'Competent'),
        (VETERAN, 'Veteran'),
        (MASTER, 'Master'),
        (ELITE, 'Elite'),
    )

    skill = models.ForeignKey('Skill', on_delete=models.SET_NULL, null=True, related_name="skill_levels")
    character = models.ForeignKey('Character', on_delete=models.SET_NULL, null=True)
    level = models.IntegerField(choices=LEVEL_CHOICES, default=NOVICE)
