from . import views
from django.contrib import admin
from django.urls import path

# importing views from views.py
from .views import index_view, gallery_view, contact_view, artsy_images_list, production_images_list, favourite_images_list

urlpatterns = [
    path('', index_view, name='index'),
    path('gallery', gallery_view, name='gallery'),
    path('contact', contact_view, name='contact'),
    path('artsy-latest', views.artsy_images_list.as_view(), name='artsy-latest'),
    path('production-latest', views.production_images_list.as_view(), name='production-latest'),
    path('favourites', views.favourite_images_list.as_view(), name='favourites'),
    # path('artsy_favourite/<slug:slug>', views.ArtsyFavourite.as_view(), name='artsy_favourite'),
    # path('production_favourite/<slug:slug>', views.ProductionFavourite.as_view(), name='production_favourite'),
]
