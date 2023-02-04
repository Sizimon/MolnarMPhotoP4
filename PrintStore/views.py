from django.shortcuts import render

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
