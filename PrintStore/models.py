from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Photos(models.Model):
    # Slug
    slug = models.SlugField(max_length=200, unique=True)
    # Image
    featured_image = CloudinaryField('image', default='placeholder')


class ArtsyPhotos(models.Model):
    # Slug
    slug = models.SlugField(max_length=200, unique=True)
    # Image
    featured_image = CloudinaryField('image', default='placeholder')


class ProductionPhotos(models.Model):
    # Slug
    slug = models.SlugField(max_length=200, unique=True)
    # Image
    featured_image = CloudinaryField('image', default='placeholder')
