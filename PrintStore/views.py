from django.shortcuts import render

# Create your views here.


def index_view(request):

    return render(request, 'index.html')


def production_view(request):

    return render(request, 'production.html')


def artsy_view(request):

    return render(request, 'artsy.html')
