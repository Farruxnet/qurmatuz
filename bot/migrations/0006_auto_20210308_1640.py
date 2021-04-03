# Generated by Django 3.1 on 2021-03-08 11:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('botconfig', '0014_viloyat_status'),
        ('bot', '0005_auto_20210308_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercart',
            name='kub',
            field=models.ManyToManyField(null=True, to='botconfig.AvtoKub'),
        ),
        migrations.AlterField(
            model_name='usercart',
            name='viloyat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='botconfig.viloyat'),
        ),
    ]