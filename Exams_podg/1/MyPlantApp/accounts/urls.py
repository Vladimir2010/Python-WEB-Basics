from django.contrib import admin
from django.urls import path, include
from .views import create, details, edit, delete

# •	http://localhost:8000/profile/create/ - profile create page
# •	http://localhost:8000/profile/details/ - profile details page
# •	http://localhost:8000/profile/edit/ - profile edit page
# •	http://localhost:8000/profile/delete/ - profile delete page



urlpatterns = [
    path('create/', catalogue, name='create-profile'),
    path('details/', create, name='profile-details'),
    path('edit/', details, name='edit-profile'),
    path('delete/', edit, name='delete-profile'),
]

