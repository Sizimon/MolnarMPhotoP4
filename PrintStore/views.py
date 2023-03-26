from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Photos, ProductionPhotos, ArtsyPhotos


# Create your views here.

# Template Views


def index_view(request):

    return render(request, 'index.html')


def gallery_view(request):

    return render(request, 'gallery.html')


def contact_view(request):

    return render(request, 'contact.html')


class artsy_images_list(generic.ListView):
    model = ArtsyPhotos
    queryset = ArtsyPhotos.objects.all()
    template_name = 'artsy_latest.html'
    context_object_name = 'ArtsyPhotos'


class production_images_list(generic.ListView):
    model = ProductionPhotos
    queryset = ProductionPhotos.objects.all()
    template_name = 'production_latest.html'
    context_object_name = 'ProductionPhotos'


class favourite_images_list(generic.ListView):
    model = Photos
    queryset = Photos.objects.filter(favourite=True)
    template_name = 'favourites.html'
    context_object_name = 'photos'


class PhotoFavourite(View):
    
    def photo(self, request, slug):
        photo = get_object_or_404(Photo, slug=slug)

        if photo.favourite.filter(id=request.user.id).exists():
            photo.favourite.remove(request.user)
        else:
            photo.favourite.add(request.user)
        
        return HttpResponseRedirect(reverse('favourite_images_list', args=[slug]))
