# Generated by Django 4.0 on 2022-09-02 12:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_list_desc10_list_desc2_list_desc3_list_desc4_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='posted',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
