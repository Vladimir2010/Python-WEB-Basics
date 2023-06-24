from django.urls import path, include
from .views import home_page, catalogue, create_car, car_details, edit_car, delete_car


urlpatterns = [
    path('', home_page, name="home_page"),
    path('catalogue/', catalogue, name="catalogue"),
    path('car/create/', create_car, name="create_car"),
    path('car/<car_id>/details', car_details, name="car_details"),
    path('car/<car_id>/edit', edit_car, name="edit_car"),
    path('car/<car_id>/delete', delete_car, name="delete_car"),
]