from django.shortcuts import render, redirect
from .models import Profile, Album
from .forms import ProfileForm, AlbumAdd


# Create your views here.

def home_page(request):
    profile = Profile.objects.first()
    albums = Album.objects.all()
    form = ProfileForm()

    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')


    context = {
        "profile": profile,
        "albums": albums,
        "add_form": form
    }

    if profile:
        return render(request, 'web/home-with-profile.html', context)
    else:
        return render(request, 'web/home-no-profile.html', context)


def add_album(request):
    profile = Profile.objects.first()
    form = AlbumAdd(request.POST or None)

    if form.is_valid():
        album = form.save(commit=False)
        album.profile = profile
        album.save()
        return redirect('home page')

    context = {
        'form': form,
        'profile': profile
    }

    return render(request, 'web/add-album.html', context)


def album_details(request, id):
    profile = Profile.objects.first()
    album = Album.objects.get(id=id)
    context = {
        'album': album,
        'profile': profile
    }
    return render(request, 'web/album-details.html', context)


def edit_album(request, id):
    profile = Profile.objects.first()
    album = Album.objects.get(id=id)
    # form = EditAlbum()
    form = AlbumAdd(instance=album)

    context = {
        'form': form,
        'profile': profile,
        'album': album
    }

    if request.method == 'POST':
        form = AlbumAdd(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('home page')

    return render(request, 'web/edit-album.html', context)


def delete_album(request, id):
    profile = Profile.objects.first()
    album = Album.objects.get(id=id)
    form = AlbumAdd(instance=album)
    context = {
        'album': album,
        'profile': profile,
        'form': form
    }

    if request.method == 'POST':
        form = AlbumAdd(request.POST, instance=album)
        if form.is_valid():
            album.delete()
            return redirect('home page')

    return render(request, 'web/delete-album.html', context)


def profile_details(request):
    profile = Profile.objects.first()
    context = {'profile': profile}
    return render(request, 'web/profile-details.html', context)


def delete_profile(request):
    profiles = Profile.objects.all()
    if request.method == 'POST':
        profiles.delete()
        return redirect('home page')
    context = {
        'profiles': profiles
    }

    return render(request, 'web/profile-delete.html', context)
