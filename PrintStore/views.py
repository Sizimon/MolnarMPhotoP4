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

# ARTSY FEATURES

class artsy_images_list(generic.ListView):
    model = ArtsyPhotos
    queryset = ArtsyPhotos.objects.all()
    template_name = 'artsy_latest.html'
    context_object_name = 'ArtsyPhotos'


# class ArtsyDetail(View):
#     def get(self, request, slug, *args, **kwargs):
#         queryset = ArtsyPhotos.objects.all()
#         photos = get_object_or_404(queryset, slug=slug)
#         favourited = False
#         if photos.favourite.filter(id=request.user.id).exists():
#             favourited = True


# class ArtsyFavourite(View):

#     def post(self, request, slug):
#         photo = get_object_or_404(ArtsyPhotos, slug=slug)

#         if photo.favourite.filter(id=request.user.id).exists():
#             photo.favourite.remove(request.user)
#         else:
#             photo.favourite.add(request.user)

#         return HttpResponseRedirect(reverse(request.path, args=[slug]))


# PRODUCTION FEATURES

class production_images_list(generic.ListView):
    model = ProductionPhotos
    queryset = ProductionPhotos.objects.all()
    template_name = 'production_latest.html'
    context_object_name = 'ProductionPhotos'


# class ProductionDetail(View):
#     def get(self, request, slug, *args, **kwargs):
#         queryset = ProdcutionPhotos.objects.all()
#         photos = get_object_or_404(queryset, slug=slug)
#         favourited = False
#         if photos.favourite.filter(id=request.user.id).exists():
#             favourited = True


# class ProductionFavourite(View):

#     def post(self, request, slug):
#         photo = get_object_or_404(ProductionPhotos, slug=slug)

#         if photo.favourite.filter(id=request.user.id).exists():
#             photo.favourite.remove(request.user)
#         else:
#             photo.favourite.add(request.user)

#         return HttpResponseRedirect(reverse(request.path, args=[slug]))


# FAVOURITE FEATURES

class favourite_images_list(generic.ListView):
    model = Photos
    queryset = Photos.objects.filter(favourite=True)
    template_name = 'favourites.html'
    context_object_name = 'photos'


# class PhotoFavourite(View):

#     def photo(self, request, slug):
#         photo = get_object_or_404(Photos, slug=slug)

#         if photo.favourite.filter(id=request.user.id).exists():
#             photo.favourite.update(request.user)
#         else:
#             photo.favourite.add(request.user)

#         return HttpResponseRedirect(reverse(request.path, args=[slug]))





