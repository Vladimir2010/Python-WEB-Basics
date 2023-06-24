from django import forms

# Create your views here.

class Name_Form(forms.Form):
    username = forms.CharField(label="Your name", max_length=10, required=False)
    email = forms.EmailField()
    password = forms.CharField()
    password2 = forms.CharField()
    Url = forms.URLField()
    date = forms.DateField()
