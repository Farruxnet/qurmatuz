# Generated by Django 3.1 on 2021-03-24 18:06

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0016_auto_20210324_2304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercart',
            name='deatline',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 25, 18, 6, 46, 737428, tzinfo=utc), verbose_name='Amal qilish vaqti'),
        ),
    ]
