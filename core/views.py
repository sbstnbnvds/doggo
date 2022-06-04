from django.shortcuts import render
from .models import Dog

# Create your views here.

def index(request):
    dogs = Dog.objects.all()
    context = {
        'dogs': dogs,
        'title': 'Index'
    }
    return render(request, 'index.html', context)


def home(request):
    return render(request, 'home.html')

def by_weight(request):
    dogs = Dog.objects.all().order_by('-weight')
    context = {
        'dogs': dogs,
        'title': 'By weight'
    }
    return render(request, 'index.html', context)

def by_breed(request):
    dogs = Dog.objects.all().order_by('breed')
    context = {
        'dogs': dogs,
        'title': 'By breed'
    }
    return render(request, 'index.html', context)
    