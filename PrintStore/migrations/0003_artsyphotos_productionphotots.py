# Generated by Django 3.2.18 on 2023-03-22 16:07

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PrintStore', '0002_auto_20230209_1528'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArtsyPhotos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('featured_image', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image')),
                ('favourite', models.IntegerField(choices=[(0, 'Not Added'), (1, 'Added')], default=0)),
            ],
        ),
        migrations.CreateModel(
            name='ProductionPhotots',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('featured_image', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image')),
                ('favourite', models.IntegerField(choices=[(0, 'Not Added'), (1, 'Added')], default=0)),
            ],
        ),
    ]
