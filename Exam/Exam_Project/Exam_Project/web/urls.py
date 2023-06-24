from django.urls import path, include
from .views import *


# •	http://localhost:8000/ - index page
# •	http://localhost:8000/dashboard/ - dashboard page
# •	http://localhost:8000/create/ - fruit create page
# •	http://localhost:8000/<fruitId>/details/ - fruit details page
# •	http://localhost:8000/<fruitId>/edit/ - fruit edit page
# •	http://localhost:8000/<fruitId>/delete/ - fruit delete page
# •	http://localhost:8000/profile/create/ - profile create page
# •	http://localhost:8000/profile/details/ - profile details page
# •	http://localhost:8000/profile/edit/ - profile edit page
# •	http://localhost:8000/profile/delete/ - profile delete page


urlpatterns = [
    path("", index, name="index"),
    path("dashboard/", dashboard, name="dashboard"),
    path("create/", create_fruit, name="fruit create"),
    path("<int:fruit_id>/", include([
        path("details/", fruit_details, name="fruit details"),
        path("edit/", fruit_edit, name="fruit edit"),
        path("delete/", fruit_delete, name="fruit delete"),
    ])),
    path("profile/create/", profile_create, name="profile create"),
    path("profile/details/", profile_details, name="profile details"),
    path("profile/edit/", profile_edit, name="profile edit"),
    path("profile/delete/", profile_delete, name="profile delete"),
]