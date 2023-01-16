# Generated by Django 4.0 on 2023-01-16 07:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('room', '0003_alter_message_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
    ]