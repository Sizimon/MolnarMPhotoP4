from django.shortcuts import render
from django.views import generic
from .models import Photos


# Create your views here.

# Template Views


def index_view(request):

    return render(request, 'index.html')


def gallery_view(request):

    return render(request, 'gallery.html')


def contact_view(request):

    return render(request, 'contact.html')


def artsy_latest_view(request):

    return render(request, 'artsy_latest.html')


def production_latest_view(request):

    return render(request, 'production_latest.html')


class favourite_images_list(generic.ListView):
    model = Photos
    favourite_image = Photos.object.filter(favourite=1)
    template_name = 'favourites.html'
