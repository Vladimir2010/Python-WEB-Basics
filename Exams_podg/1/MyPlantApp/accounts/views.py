from django.shortcuts import render


# create, details, edit, delete
# Create your views here.


def create(request):
    return render(request, template_name='templates/create-profile.html')


def details(request):
    return render(request, template_name='templates/profile-details.html')


def edit(request):
    return render(request, template_name='templates/edit-profile.html')


def delete(request):
    return render(request, template_name='templates/delete-profile.html')
