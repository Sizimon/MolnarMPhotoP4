from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

FAVOURITE = ((0, 'Not Added'), (1, 'Added'))


class favouriteImage(models.Model):
    # Image
    featured_image = models.CloudinaryField('image')
    favourite = models.IntegerField(choices=FAVOURITE, default=0)
