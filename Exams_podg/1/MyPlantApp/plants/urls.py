from django.contrib import admin
from django.urls import path, include
from .views import home, catalogue, create, details, edit, delete


# •	http://localhost:8000/catalogue/ - catalogue
# •	http://localhost:8000/create/ - plant create page
# •	http://localhost:8000/details/<plant_id>/ - plant details page
# •	http://localhost:8000/edit/<plant_id>/ - plant edit page
# •	http://localhost:8000/delete/<plant_id>/ - plant delete page



urlpatterns = [
    path('', home, name='home-page'),
    path('catalogue/', catalogue, name='catalogue'),
    path('create/', create, name='create-plant'),
    path('details/<int:plant_id/>', details, name='details-plant'),
    path('edit/<int:plant_id>/', edit, name='edit-plant'),
    path('delete/<int:plant_id>/', delete, name='delete-plant')
]
