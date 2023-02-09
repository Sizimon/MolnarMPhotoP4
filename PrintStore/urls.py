from . import views
from django.contrib import admin
from django.urls import path

# importing views from views..py
from .views import index_view, gallery_view, contact_view, artsy_latest_view, production_latest_view, favourite_images_list

urlpatterns = [
    path('', index_view, name='index'),
    path('gallery', gallery_view, name='gallery'),
    path('contact', contact_view, name='contact'),
    path('artsy-latest', artsy_latest_view, name='artsy-latest'),
    path('production-latest', production_latest_view, name='production-latest'),
    path('favourites', views.favourite_images_list.as_view(), name='favourites')
]
