# Generated by Django 3.2.8 on 2021-10-15 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hospital_2', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospitals',
            name='hirurg',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='hospitals',
            name='terapevt',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
