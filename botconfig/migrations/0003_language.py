# Generated by Django 3.1 on 2021-02-17 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('botconfig', '0002_auto_20210216_2159'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('lan', models.CharField(choices=[('oz', "O'zbek"), ('uz', 'Узбек'), ('ru', 'Руский')], max_length=30)),
                ('key', models.CharField(max_length=30)),
            ],
        ),
    ]
