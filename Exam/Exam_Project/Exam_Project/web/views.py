from django.shortcuts import render, redirect
from .forms import *
from .models import *



# Create your views here.
def index(request):
    profile = Profile.objects.first()

    context = {
        'profile': profile
    }

    return render(request, "web/index.html", context)

def dashboard(request):
    fruits = Fruit.objects.all()
    profile = Profile.objects.first()
    context = {
        'fruits': fruits,
        'profile': profile
    }
    return render(request, "web/dashboard.html", context)

def create_fruit(request):
    form = FruitForm()
    profile = Profile.objects.first()
    if request.method == 'POST':
        form = FruitForm(request.POST)
        if form.is_valid():
            fruit = form.save(commit=False)
            fruit.profile = profile
            fruit.save()
            return redirect('dashboard')
    context = {
        'profile': profile,
        'form': form
    }
    return render(request, 'web/create-fruit.html', context)


def fruit_details(request, fruit_id):
    profile = Profile.objects.first()
    fruit = Fruit.objects.get(id=fruit_id)
    context = {
        'fruit': fruit,
        'profile': profile
    }
    return render(request, "web/details-fruit.html", context)


def fruit_edit(request, fruit_id):
    profile = Profile.objects.first()
    fruit = Fruit.objects.get(id=fruit_id)
    form = FruitEditForm(instance=fruit)
    if request.method == 'POST':
        form = FruitEditForm(request.POST, instance=fruit)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context = {
        'form': form,
        'profile': profile,
        'fruit': fruit
    }
    return render(request, 'web/edit-fruit.html', context)


def fruit_delete(request, fruit_id):
    profile = Profile.objects.first()
    fruit = Fruit.objects.get(id=fruit_id)
    form = DeleteFruitForm(instance=fruit)
    if request.method == 'POST':
        form = DeleteFruitForm(request.POST, instance=fruit)
        if form.is_valid():
            fruit.delete()
            return redirect('dashboard')
    context = {
        'fruit': fruit,
        'profile': profile,
        'form': form
    }
    return render(request, "web/delete-fruit.html", context)


def profile_create(request):
    form = CreateProfileForm()
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context = {
        'form': form
    }
    return render(request, "web/create-profile.html", context)


def profile_details(request):
    profile = Profile.objects.first()
    profile_image = profile.image_url
    context = {
        'profile': profile,
        'profile_image': profile_image
    }
    return render(request, "web/details-profile.html", context)

def profile_edit(request):
    profile = Profile.objects.first()
    form = EditProfileForm(instance=profile)
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile details')
    context = {
        'profile': profile,
        'form': form
    }
    return render(request, "web/edit-profile.html", context)

def profile_delete(request):
    profile = Profile.objects.first()
    if request.method == 'POST':
        profile.delete()
        return redirect('index')
    context = {
        'profile': profile
    }
    return render(request, "web/delete-profile.html", context)