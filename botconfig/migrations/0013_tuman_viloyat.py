# Generated by Django 3.1 on 2021-03-07 18:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('botconfig', '0012_auto_20210307_2308'),
    ]

    operations = [
        migrations.AddField(
            model_name='tuman',
            name='viloyat',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='botconfig.viloyat'),
            preserve_default=False,
        ),
    ]
