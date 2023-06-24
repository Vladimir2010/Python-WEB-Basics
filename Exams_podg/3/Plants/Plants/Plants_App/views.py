from django.shortcuts import render
from .models import Plant

# Create your views here.


def home(request):
    return render(request, 'home-page.html')


def catalogue(request):
    plants = Plant.objects.all()
    context = {'plants': plants}
    return render(request, 'catalogue.html', context=context)


def create(request):
    return render(request, 'create-plant.html')


def details(request):
    return render(request, 'plant-details.html')


def edit(request):
    return render(request, 'edit-plant.html')


def delete(request):
    return render(request, 'delete-plant.html')
