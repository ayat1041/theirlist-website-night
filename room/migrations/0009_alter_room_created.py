# Generated by Django 4.0 on 2023-01-17 14:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0008_room_capacity_room_password_room_topic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
    ]
