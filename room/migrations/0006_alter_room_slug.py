# Generated by Django 4.0 on 2023-01-16 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0005_room_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
