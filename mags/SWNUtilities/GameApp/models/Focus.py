from django.db import models


class Focus(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class FocusLevel(models.Model):
    FOCUS_LV_1 = 1
    FOCUS_LV_2 = 2
    FOCUS_LEVEL = (
        (FOCUS_LV_1, '1'),
        (FOCUS_LV_2, '2'),
    )
    level = models.PositiveSmallIntegerField(
            choices=FOCUS_LEVEL,
            default=FOCUS_LV_1,
        )
    focus = models.ForeignKey(
        'Focus',
        on_delete=models.CASCADE,
    )
    character = models.ForeignKey(
        'Character',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return "{}_{}".format(self.focus.__str__(), self.level.__str__())


class FocusAbility(models.Model):
    description = models.TextField()
    FOCUS_LV_1 = 1
    FOCUS_LV_2 = 2
    FOCUS_LEVEL = (
        (FOCUS_LV_1, '1'),
        (FOCUS_LV_2, '2'),
    )
    level = models.PositiveSmallIntegerField(choices=FOCUS_LEVEL)
    focus = models.ForeignKey(
        'Focus',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return "{}_{}".format(self.focus.__str__(), self.level.__str__())
