# Generated by Django 3.2.4 on 2021-06-26 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GameApp', '0010_alter_party_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]