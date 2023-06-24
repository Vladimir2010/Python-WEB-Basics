from django.urls import path, include
from . import views

# add, details, edit, delete
#<str:username>/pet/<slug:pet_name>/

urlpatterns = [
    path('add/', views.add, name='add-pet'),
    path('<str:username>/pet/<slug:pet_name>/', include([
        path('', views.details, name='details'),
        path('edit/', views.edit, name='edit'),
        path('delete/', views.delete, name='delete'),
    ])),

]