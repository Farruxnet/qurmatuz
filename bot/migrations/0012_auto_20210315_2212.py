# Generated by Django 3.1 on 2021-03-15 17:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0011_auto_20210315_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercart',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 15, 22, 12, 5, 257066)),
        ),
        migrations.AlterField(
            model_name='usercart',
            name='deatline',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 30, 22, 12, 5, 257066)),
        ),
    ]
