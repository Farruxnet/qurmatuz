# Generated by Django 3.1 on 2021-03-21 17:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('botconfig', '0018_auto_20210315_2212'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='avto',
            options={'verbose_name': 'Avtomobillar', 'verbose_name_plural': 'Avtomobillar'},
        ),
        migrations.AlterModelOptions(
            name='avtokub',
            options={'verbose_name': "Avtomobil sig'imi", 'verbose_name_plural': "Avtomobil sig'imi"},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': "Bo'limlar", 'verbose_name_plural': "Bo'limlar"},
        ),
        migrations.AlterModelOptions(
            name='config',
            options={'verbose_name': 'Bot sozlamalari', 'verbose_name_plural': 'Bot sozlamalari'},
        ),
        migrations.AlterModelOptions(
            name='paket',
            options={'verbose_name': 'Tariflar (paket)', 'verbose_name_plural': 'Tariflar (paket)'},
        ),
        migrations.AlterModelOptions(
            name='podcategory',
            options={'verbose_name': "Kichik bo'limlar (podkategoryalar)", 'verbose_name_plural': "Kichik bo'limlar (podkategoryalar)"},
        ),
        migrations.AlterModelOptions(
            name='startnarx',
            options={'verbose_name': "Boshlang'ich narxlar", 'verbose_name_plural': "Boshlang'ich narxlar"},
        ),
        migrations.AlterModelOptions(
            name='tuman',
            options={'verbose_name': 'Tumanlar', 'verbose_name_plural': 'Tumanlar'},
        ),
        migrations.AlterModelOptions(
            name='viloyat',
            options={'verbose_name': 'Viloyatlar', 'verbose_name_plural': 'Viloyatlar'},
        ),
        migrations.AlterField(
            model_name='avto',
            name='kub',
            field=models.ManyToManyField(to='botconfig.AvtoKub', verbose_name="Avtomobil sig'imi. bir nechta tanlash mumkin ctrl tugamsini bosgan holatda."),
        ),
        migrations.AlterField(
            model_name='avto',
            name='oz',
            field=models.CharField(max_length=80, unique=True, verbose_name="O'zbek"),
        ),
        migrations.AlterField(
            model_name='avto',
            name='ru',
            field=models.CharField(max_length=80, unique=True, verbose_name='Rus'),
        ),
        migrations.AlterField(
            model_name='avto',
            name='uz',
            field=models.CharField(max_length=80, unique=True, verbose_name='Krill'),
        ),
        migrations.AlterField(
            model_name='avtokub',
            name='kub',
            field=models.IntegerField(verbose_name="Avtomobil sig'imi"),
        ),
        migrations.AlterField(
            model_name='category',
            name='oz',
            field=models.CharField(max_length=80, unique=True, verbose_name="O'zbek"),
        ),
        migrations.AlterField(
            model_name='category',
            name='ru',
            field=models.CharField(max_length=80, unique=True, verbose_name='Rus'),
        ),
        migrations.AlterField(
            model_name='category',
            name='uz',
            field=models.CharField(max_length=80, unique=True, verbose_name='Krill'),
        ),
        migrations.AlterField(
            model_name='config',
            name='about',
            field=models.TextField(verbose_name='Haqida'),
        ),
        migrations.AlterField(
            model_name='config',
            name='contact',
            field=models.TextField(verbose_name="Aloqa ma'lumotlari"),
        ),
        migrations.AlterField(
            model_name='config',
            name='text',
            field=models.TextField(verbose_name='Start matni'),
        ),
        migrations.AlterField(
            model_name='config',
            name='video',
            field=models.TextField(verbose_name="Foydalanish yo'riqnomas videosi manzili"),
        ),
        migrations.AlterField(
            model_name='config',
            name='whouse',
            field=models.TextField(verbose_name='Qanday foydalaniladi?'),
        ),
        migrations.AlterField(
            model_name='paket',
            name='day',
            field=models.IntegerField(default=0, verbose_name='Amal qilish vaqti (kun)'),
        ),
        migrations.AlterField(
            model_name='paket',
            name='name_oz',
            field=models.CharField(max_length=80, unique=True, verbose_name="O'zbek"),
        ),
        migrations.AlterField(
            model_name='paket',
            name='name_ru',
            field=models.CharField(max_length=80, unique=True, verbose_name='Rus'),
        ),
        migrations.AlterField(
            model_name='paket',
            name='name_uz',
            field=models.CharField(max_length=80, unique=True, verbose_name='Krill'),
        ),
        migrations.AlterField(
            model_name='paket',
            name='price',
            field=models.CharField(max_length=80, unique=True, verbose_name='Narxi (sum)'),
        ),
        migrations.AlterField(
            model_name='podcategory',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='botconfig.category', verbose_name="Bo'limni tanlang"),
        ),
        migrations.AlterField(
            model_name='podcategory',
            name='oz',
            field=models.CharField(max_length=80, unique=True, verbose_name="O'zbek"),
        ),
        migrations.AlterField(
            model_name='podcategory',
            name='ru',
            field=models.CharField(max_length=80, unique=True, verbose_name='Rus'),
        ),
        migrations.AlterField(
            model_name='podcategory',
            name='uz',
            field=models.CharField(max_length=80, unique=True, verbose_name='Krill'),
        ),
        migrations.AlterField(
            model_name='startnarx',
            name='narx',
            field=models.CharField(max_length=50, verbose_name="Boshlang'ich narx"),
        ),
        migrations.AlterField(
            model_name='tuman',
            name='oz',
            field=models.CharField(max_length=80, unique=True, verbose_name="O'zbek"),
        ),
        migrations.AlterField(
            model_name='tuman',
            name='ru',
            field=models.CharField(max_length=80, unique=True, verbose_name='Rus'),
        ),
        migrations.AlterField(
            model_name='tuman',
            name='uz',
            field=models.CharField(max_length=80, unique=True, verbose_name='Krill'),
        ),
        migrations.AlterField(
            model_name='tuman',
            name='viloyat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='botconfig.viloyat', verbose_name='Viloyatni tanlang'),
        ),
        migrations.AlterField(
            model_name='viloyat',
            name='oz',
            field=models.CharField(max_length=80, unique=True, verbose_name="O'zbek"),
        ),
        migrations.AlterField(
            model_name='viloyat',
            name='ru',
            field=models.CharField(max_length=80, unique=True, verbose_name='Rus'),
        ),
        migrations.AlterField(
            model_name='viloyat',
            name='status',
            field=models.BooleanField(default=False, verbose_name='Holati'),
        ),
        migrations.AlterField(
            model_name='viloyat',
            name='uz',
            field=models.CharField(max_length=80, unique=True, verbose_name='Krill'),
        ),
    ]
