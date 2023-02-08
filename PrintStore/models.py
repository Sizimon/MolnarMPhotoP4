from django.db import models
from django.contrib.auth.models import User

# Create your models here.

FAVOURITE = ((0, 'Not Added'), (1, 'Added'))


class FavouriteImage(models.Model):
    # Image
    featured_image = models.CloudinaryField('image')
    favourite = models.IntegerField(choices=FAVOURITE, default=0)
