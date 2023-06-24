from django.shortcuts import render
from .forms import Name_Form


def index(request):
    if request.method == 'POST':
        form = Name_Form(request.POST)
    if form.is_valid:
        name = form.cleaned_data["your_name"]
    else:
        form = Name_Form()
    context = {
        'form': form,
        'name': name,
    }
    return render(request, 'web/index.html', context)