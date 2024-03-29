# Generated by Django 3.1 on 2021-03-21 17:25

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('botconfig', '0019_auto_20210321_2225'),
        ('bot', '0012_auto_20210315_2212'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tguser',
            options={'verbose_name': 'Foydalanuvchilar', 'verbose_name_plural': 'Foydalanuvchilar'},
        ),
        migrations.AlterModelOptions(
            name='usercart',
            options={'verbose_name': "Foydalanuvchilar e'lonlari", 'verbose_name_plural': "Foydalanuvchilar e'lonlari"},
        ),
        migrations.AlterField(
            model_name='usercart',
            name='avto',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='botconfig.avto', verbose_name='Avtomobil'),
        ),
        migrations.AlterField(
            model_name='usercart',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='botconfig.category', verbose_name="Bo'lim"),
        ),
        migrations.AlterField(
            model_name='usercart',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name="Qo'shilgan vaqti"),
        ),
        migrations.AlterField(
            model_name='usercart',
            name='deatline',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 22, 17, 25, 26, 5324, tzinfo=utc), verbose_name='Amal qilish vaqti'),
        ),
        migrations.AlterField(
            model_name='usercart',
            name='kub',
            field=models.ManyToManyField(null=True, to='botconfig.AvtoKub', verbose_name="Avtomobil sig'imi"),
        ),
        migrations.AlterField(
            model_name='usercart',
            name='narx',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='botconfig.startnarx', verbose_name="Boshlang'ich narx"),
        ),
        migrations.AlterField(
            model_name='usercart',
            name='paket',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='botconfig.paket', verbose_name='Tarif'),
        ),
        migrations.AlterField(
            model_name='usercart',
            name='podcategory',
            field=models.ManyToManyField(null=True, to='botconfig.PodCategory', verbose_name='Podkategoryalar'),
        ),
        migrations.AlterField(
            model_name='usercart',
            name='status',
            field=models.BooleanField(default=False, verbose_name='Holati'),
        ),
        migrations.AlterField(
            model_name='usercart',
            name='telefon',
            field=models.CharField(max_length=25, null=True, verbose_name='Telefon raqam'),
        ),
        migrations.AlterField(
            model_name='usercart',
            name='tuman',
            field=models.ManyToManyField(null=True, to='botconfig.Tuman', verbose_name='Tumanlar'),
        ),
        migrations.AlterField(
            model_name='usercart',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bot.tguser', verbose_name='Foydalanuvchi'),
        ),
        migrations.AlterField(
            model_name='usercart',
            name='username',
            field=models.CharField(max_length=50, null=True, verbose_name='Telegram username'),
        ),
        migrations.AlterField(
            model_name='usercart',
            name='viloyat',
            field=models.ManyToManyField(null=True, to='botconfig.Viloyat', verbose_name='Viloyatlar'),
        ),
    ]
