# Generated by Django 3.2.4 on 2021-07-04 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GameApp', '0015_auto_20210701_2255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='background',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='background',
            name='heading',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]