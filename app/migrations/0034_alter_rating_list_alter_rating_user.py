# Generated by Django 4.0 on 2022-10-25 10:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('app', '0033_rating_musicrating_bookrating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='list',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.list'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
    ]
