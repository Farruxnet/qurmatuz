# Generated by Django 3.1 on 2021-02-28 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('botconfig', '0006_avto_avtokub_tuman_viloyat'),
    ]

    operations = [
        migrations.AddField(
            model_name='avto',
            name='lan',
            field=models.CharField(choices=[('oz', "O'zbek"), ('uz', 'Узбек'), ('ru', 'Руский')], default='12', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tuman',
            name='lan',
            field=models.CharField(choices=[('oz', "O'zbek"), ('uz', 'Узбек'), ('ru', 'Руский')], default='454', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='viloyat',
            name='lan',
            field=models.CharField(choices=[('oz', "O'zbek"), ('uz', 'Узбек'), ('ru', 'Руский')], default='as', max_length=30),
            preserve_default=False,
        ),
    ]