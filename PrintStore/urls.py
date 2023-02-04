from django.contrib import admin
from django.urls import path

# importing views from views..py
from .views import index_view, production_view, artsy_view, contact_view, artsy_latest_view

urlpatterns = [
    path('', index_view, name='index'),
    path('production', production_view, name='production'),
    path('artsy', artsy_view, name='artsy'),
    path('contact', contact_view, name='contact'),
    path('artsy-latest', artsy_latest_view, name='artsy-latest')
]
