from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

FAVOURITE = ((False, 'Not Added'), (True, 'Added'))


class Photos(models.Model):
    # Slug
    slug = models.SlugField(max_length=200, unique=True)
    # Image
    featured_image = CloudinaryField('image', default='placeholder')
    # Favourite Status
    favourite = models.IntegerField(choices=FAVOURITE, default=False)


class ArtsyPhotos(models.Model):
    # Slug
    slug = models.SlugField(max_length=200, unique=True)
    # Image
    featured_image = CloudinaryField('image', default='placeholder')
    # Favourite Status
    favourite = models.IntegerField(choices=FAVOURITE, default=False)


class ProductionPhotos(models.Model):
    # Slug
    slug = models.SlugField(max_length=200, unique=True)
    # Image
    featured_image = CloudinaryField('image', default='placeholder')
    # Favourite Status
    favourite = models.IntegerField(choices=FAVOURITE, default=False)
