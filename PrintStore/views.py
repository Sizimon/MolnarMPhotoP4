from django.shortcuts import render

# Create your views here.

# Template Views


def index_view(request):

    return render(request, 'index.html')


def production_view(request):

    return render(request, 'production.html')


def artsy_view(request):

    return render(request, 'artsy.html')


def contact_view(request):

    return render(request, 'contact.html')


def artsy_latest_view(request):

    return render(request, 'artsy_latest.html')
