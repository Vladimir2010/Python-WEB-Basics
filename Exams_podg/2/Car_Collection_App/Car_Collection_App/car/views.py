from django.shortcuts import render

# Create your views here.\


def home_page(request):
    return render(request, 'index.html')


def catalogue(request):
    pass


def create_car(request):
    pass


def car_details(request, car_id):
    pass


def edit_car(request, car_id):
    pass


def delete_car(request, car_id):
    pass


