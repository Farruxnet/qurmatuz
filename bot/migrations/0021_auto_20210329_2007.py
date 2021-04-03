# Generated by Django 3.1 on 2021-03-29 15:07

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0020_auto_20210328_0035'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usercart',
            options={'ordering': ['id'], 'verbose_name': "Foydalanuvchilar e'lonlari", 'verbose_name_plural': "Foydalanuvchilar e'lonlari"},
        ),
        migrations.AlterField(
            model_name='usercart',
            name='deatline',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 30, 15, 7, 6, 246409, tzinfo=utc), verbose_name='Amal qilish vaqti'),
        ),
    ]
