from django.urls import path, include
from . import views

urlpatterns = [
    path('add/', views.add, name='add'),
    path('<int:pk>', include([
        path('', views.details, name='details'),
        path('edit/', views.edit, name='edit'),
    ]))

]