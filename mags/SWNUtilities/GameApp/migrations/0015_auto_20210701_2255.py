# Generated by Django 3.2.4 on 2021-07-02 05:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GameApp', '0014_auto_20210701_2018'),
    ]

    operations = [
        migrations.CreateModel(
            name='Background',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True, unique=True)),
                ('heading', models.TextField(max_length=200, null=True)),
                ('description', models.TextField(null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='character',
            name='attributes',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='character_attributes', to='GameApp.attributes'),
        ),
        migrations.AddField(
            model_name='character',
            name='background',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='character_backgrounds', to='GameApp.background'),
        ),
    ]
