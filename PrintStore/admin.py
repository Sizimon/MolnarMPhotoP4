from django.contrib import admin
from .models import Photos, ProductionPhotos, ArtsyPhotos
# Register your models here.

class PhotosAdmin(admin.ModelAdmin):
    list_display = ["featured_image","slug"]

class ArtsyPhotosAdmin(admin.ModelAdmin):
    list_display = ["featured_image","slug"]


admin.site.register(Photos, PhotosAdmin)
admin.site.register(ProductionPhotos)
admin.site.register(ArtsyPhotos, ArtsyPhotosAdmin)
