# Generated by Django 3.1 on 2021-02-28 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tguser',
            name='step',
            field=models.IntegerField(default=0),
        ),
    ]