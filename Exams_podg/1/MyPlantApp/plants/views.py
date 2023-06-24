from django.shortcuts import render

# Create your views here.

def home(request):
    profile = ProfileModel.objects.first()
    context = {'profile': profile}
    return render(request, template_name='templates/home-page.html', context=context)


def catalogue(request):
    return render(request, template_name='templates/catalogue.html')


def create(request):
    return render(request, template_name='templates/create-plant.html')


def details(request, plant_id):
    return render(request, template_name='templates/plant-details.html')


def edit(request, plant_id):
    return render(request, template_name='templates/edit-plant.html')


def delete(request, plant_id):
    return render(request, template_name='templates/delete-plant.html')

