# Generated by Django 3.1 on 2021-02-22 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('botconfig', '0004_auto_20210222_1051'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='config',
            name='youtubelink',
        ),
        migrations.AddField(
            model_name='config',
            name='video',
            field=models.TextField(default='1'),
            preserve_default=False,
        ),
    ]
