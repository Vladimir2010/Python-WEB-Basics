from django.shortcuts import render


def add(request):
    return render(request, template_name='pets/pet-add-page.html')


def details(request):
    return reneder(request, template_name='pets/pet-details-page.html')


def edit(request):
    return render(request, template_name='pets/pet-edit-page.html')


def delete(request):
    return render(request, template_name='pets/pet-delete-page.html')


# Create your views here.
