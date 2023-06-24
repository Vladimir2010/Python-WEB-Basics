from django.shortcuts import render, redirect
from .forms import RegisterProfile


def create(request):
    if request.method == 'POST':
        form = RegisterProfile(request.POST)

        if form.is_valid():
            form.save()
            return redirect(to='//catalogue/')
    else:
        form = RegisterProfile()
    context = {'form': form}

    return render(request, 'create-profile.html', context=context)


def details(request):
    return render(request, 'profile-details.html')


def edit(request):
    return render(request, 'edit-profile.html')


def delete(request):
    return render(request, 'delete-profile.html')




# Create your views here.
