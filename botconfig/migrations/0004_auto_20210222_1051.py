# Generated by Django 3.1 on 2021-02-22 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('botconfig', '0003_language'),
    ]

    operations = [
        migrations.CreateModel(
            name='Config',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('youtubelink', models.CharField(max_length=255)),
                ('about', models.TextField()),
                ('contact', models.TextField()),
                ('whouse', models.TextField()),
                ('lan', models.CharField(choices=[('oz', "O'zbek"), ('uz', 'Узбек'), ('ru', 'Руский')], max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='Lan',
        ),
        migrations.DeleteModel(
            name='Language',
        ),
    ]
