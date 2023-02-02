from django.contrib import admin
from django.urls import path

# importing views from views..py
from .views import index_view

urlpatterns = [
    path('', index_view, name='index'),
]
