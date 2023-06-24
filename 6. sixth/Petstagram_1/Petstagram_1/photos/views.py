from django.shortcuts import render


def add(request):
    return render(request, template_name='photos/photo-add-page.html')


def details(request):
    return render(request, template_name='photos/photo-details-page.html')


def edit(request):
    return render(request, template_name='photos/photo-edit-page.html')
# Create your views here.
