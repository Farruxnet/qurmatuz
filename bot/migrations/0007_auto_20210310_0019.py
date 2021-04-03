# Generated by Django 3.1 on 2021-03-09 19:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('botconfig', '0014_viloyat_status'),
        ('bot', '0006_auto_20210308_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercart',
            name='avto',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='botconfig.avto'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='usercart',
            name='kub',
            field=models.ManyToManyField(to='botconfig.AvtoKub'),
        ),
        migrations.RemoveField(
            model_name='usercart',
            name='podcategory',
        ),
        migrations.AddField(
            model_name='usercart',
            name='podcategory',
            field=models.ManyToManyField(to='botconfig.PodCategory'),
        ),
        migrations.AlterField(
            model_name='usercart',
            name='viloyat',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='botconfig.viloyat'),
            preserve_default=False,
        ),
    ]