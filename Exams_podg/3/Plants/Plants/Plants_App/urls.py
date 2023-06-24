from django.urls import path, include
from .views import home, catalogue, create, details, edit, delete
"""
•	http://localhost:8000/ - home page
•	http://localhost:8000/catalogue/ - catalogue
•	http://localhost:8000/create/ - plant create page
•	http://localhost:8000/details/<plant_id>/ - plant details page
•	http://localhost:8000/edit/<plant_id>/ - plant edit page
•	http://localhost:8000/delete/<plant_id>/ - plant delete page"""

urlpatterns = [
    path('', home, name='home'),
    path('catalogue/', catalogue, name='catalogue'),
    path('create/', create, name='create'),
    path('details/<plant_id>/', details, name='details'),
    path('edit/<plant_id>/', edit, name='edit'),
    path('delete/<plant_id>/', delete, name='delete'),
]