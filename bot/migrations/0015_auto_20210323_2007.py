# Generated by Django 3.1 on 2021-03-23 15:07

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0014_auto_20210321_2236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercart',
            name='deatline',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 24, 15, 7, 37, 556650, tzinfo=utc), verbose_name='Amal qilish vaqti'),
        ),
    ]
