from django.db import models


class Character(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    str = models.PositiveSmallIntegerField()
    dex = models.PositiveSmallIntegerField()
    con = models.PositiveSmallIntegerField()
    int = models.PositiveSmallIntegerField()
    cha = models.PositiveSmallIntegerField()
    hit_point_max = models.PositiveSmallIntegerField()
    hit_points = models.SmallIntegerField()
    background = models.ForeignKey('Background', on_delete=models.CASCADE)
    species = models.ForeignKey('Species', on_delete=models.CASCADE)
    pronouns = models.ForeignKey('Pronouns', on_delete=models.CASCADE)
    skills = models.ManyToManyField('Skill', through='SkillLevel')
    char_class = models.ForeignKey('CharClass', on_delete=models.CASCADE)
    foci = models.ManyToManyField('Focus', through='FocusLevel')
    experience = models.PositiveSmallIntegerField(null=True)
    level = models.PositiveSmallIntegerField(null=True)
    credits = models.IntegerField(null=True)

    def __str__(self):
        return self.name


