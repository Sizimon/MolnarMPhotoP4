# Generated by Django 3.2.19 on 2023-05-08 12:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PrintStore', '0007_auto_20230403_1600'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artsyphotos',
            name='favourite',
        ),
        migrations.RemoveField(
            model_name='photos',
            name='favourite',
        ),
        migrations.RemoveField(
            model_name='productionphotos',
            name='favourite',
        ),
    ]
