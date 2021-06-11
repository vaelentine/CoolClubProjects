# Generated by Django 3.2.4 on 2021-06-11 21:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CharacterManager', '0003_pronouns_gender_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='charclass',
            name='abilities',
        ),
        migrations.AddField(
            model_name='character',
            name='credits',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='experience',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='level',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='charclass',
            name='ability',
            field=models.ManyToManyField(related_name='charclasses', to='CharacterManager.ClassAbility'),
        ),
        migrations.AlterField(
            model_name='skilllevel',
            name='level',
            field=models.IntegerField(choices=[(0, 'Novice'), (1, 'Competent'), (2, 'Veteran'), (3, 'Master'), (4, 'Elite')], default=0),
        ),
        migrations.AlterField(
            model_name='skilllevel',
            name='skill',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='skill_levels', to='CharacterManager.skill'),
        ),
    ]
