# Generated by Django 3.1 on 2021-03-07 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('botconfig', '0011_auto_20210307_2121'),
    ]

    operations = [
        migrations.RenameField(
            model_name='avto',
            old_name='name',
            new_name='oz',
        ),
        migrations.RemoveField(
            model_name='avto',
            name='lan',
        ),
        migrations.RemoveField(
            model_name='tuman',
            name='lan',
        ),
        migrations.RemoveField(
            model_name='tuman',
            name='name',
        ),
        migrations.RemoveField(
            model_name='tuman',
            name='viloyat',
        ),
        migrations.RemoveField(
            model_name='viloyat',
            name='lan',
        ),
        migrations.RemoveField(
            model_name='viloyat',
            name='name',
        ),
        migrations.AddField(
            model_name='avto',
            name='ru',
            field=models.CharField(default='asd', max_length=80, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='avto',
            name='uz',
            field=models.CharField(default='asd', max_length=80, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tuman',
            name='oz',
            field=models.CharField(default='asd', max_length=80, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tuman',
            name='ru',
            field=models.CharField(default='asd', max_length=80, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tuman',
            name='uz',
            field=models.CharField(default='asd', max_length=80, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='viloyat',
            name='oz',
            field=models.CharField(default='asd', max_length=80, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='viloyat',
            name='ru',
            field=models.CharField(default='asd', max_length=80, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='viloyat',
            name='uz',
            field=models.CharField(default='asd', max_length=80, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='oz',
            field=models.CharField(max_length=80, unique=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='ru',
            field=models.CharField(max_length=80, unique=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='uz',
            field=models.CharField(max_length=80, unique=True),
        ),
        migrations.AlterField(
            model_name='podcategory',
            name='oz',
            field=models.CharField(max_length=80, unique=True),
        ),
        migrations.AlterField(
            model_name='podcategory',
            name='ru',
            field=models.CharField(max_length=80, unique=True),
        ),
        migrations.AlterField(
            model_name='podcategory',
            name='uz',
            field=models.CharField(max_length=80, unique=True),
        ),
    ]