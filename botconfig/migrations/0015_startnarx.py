# Generated by Django 3.1 on 2021-03-14 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('botconfig', '0014_viloyat_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='StartNarx',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('narx', models.IntegerField(default=0)),
            ],
        ),
    ]
