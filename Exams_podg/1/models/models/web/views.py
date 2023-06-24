from django.shortcuts import render
from .models import Employee

# Create your views here.


def index(request):

    employee = Employee.objects.all()
    print(employee)

    return render(request, template_name='web/index.html')
