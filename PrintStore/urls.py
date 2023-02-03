from django.contrib import admin
from django.urls import path

# importing views from views..py
from .views import index_view, production_view

urlpatterns = [
    path('', index_view, name='index'),
    path('production', production_view, name='production'),
]
