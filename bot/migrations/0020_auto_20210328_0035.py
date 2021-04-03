# Generated by Django 3.1 on 2021-03-27 19:35

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('botconfig', '0022_auto_20210324_2306'),
        ('bot', '0019_auto_20210327_0106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercart',
            name='deatline',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 28, 19, 35, 8, 545213, tzinfo=utc), verbose_name='Amal qilish vaqti'),
        ),
        migrations.AlterField(
            model_name='usercart',
            name='narx',
            field=models.ForeignKey(help_text='--------- belgi kelishilgan narx', null=True, on_delete=django.db.models.deletion.CASCADE, to='botconfig.startnarx', verbose_name="Boshlang'ich narx"),
        ),
    ]