# Generated by Django 3.1 on 2021-03-26 20:06

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0018_auto_20210326_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercart',
            name='deatline',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 27, 20, 6, 8, 743764, tzinfo=utc), verbose_name='Amal qilish vaqti'),
        ),
    ]
