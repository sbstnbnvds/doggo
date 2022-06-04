from django.shortcuts import render
from .models import Dog

# Create your views here.

def index(request):
    dogs = Dog.objects.all()
    context = {
        'dogs': dogs
    }
    return render(request, 'index.html', context)


def home(request):
    return render(request, 'home.html')