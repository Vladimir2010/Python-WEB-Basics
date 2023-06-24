from django.urls import path, include
from .views import create, details, edit, delete

"""
•	http://localhost:8000/profile/create/ - profile create page
•	http://localhost:8000/profile/details/ - profile details page
•	http://localhost:8000/profile/edit/ - profile edit page
•	http://localhost:8000/profile/delete/ - profile delete page"""

urlpatterns = [
    path('create/', create, name='create_profile'),
    path('details/', details, name='profile_details'),
    path('edit/', edit, name='edit_profile'),
    path('delete/', delete, name='delete_profile'),
]
