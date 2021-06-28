# Generated by Django 3.2.4 on 2021-06-28 05:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GameApp', '0011_alter_player_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='attributes',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='character_attributes', to='GameApp.attributes'),
        ),
    ]
