from django import forms
from .models import *


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['age', 'image_url']
        labels = {
            'first_name': '',
            'last_name': '',
            'email': '',
            'password': '',
        }
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'First Name',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Last Name',
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Email',
                }
            ),
            'password': forms.PasswordInput(
                attrs={
                    'placeholder': 'Password',
                }
            )
        }


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'image_url', 'age']
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'First Name',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Last Name',
                }
            ),
            'image_url': forms.URLInput(
                attrs={
                    'placeholder': 'Image URL',
                }
            ),
            'age': forms.NumberInput(
                attrs={
                    'placeholder': 'Age',
                }
            )
        }

class FruitForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = '__all__'
        exclude = ['profile']
        labels = {
            'name': '',
            'image_url': '',
            'description': '',
            'nutrition': '',
        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Fruit Name',
                }
            ),
            'image_url': forms.URLInput(
                attrs={
                    'placeholder': 'Fruit Image URL',
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Fruit Description',
                }
            ),
            'nutrition': forms.Textarea(
                attrs={
                    'placeholder': 'Nutrition Info',
                }
            ),
        }

class FruitEditForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = '__all__'
        exclude = ['profile']
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Fruit Name',
                }
            ),
            'image_url': forms.URLInput(
                attrs={
                    'placeholder': 'Fruit Image URL',
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Fruit Description',
                }
            ),
            'nutrition': forms.Textarea(
                attrs={
                    'placeholder': 'Nutrition Info',
                }
            ),
        }


class DeleteFruitForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = '__all__'
        exclude = ['nutrition', 'profile']
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Fruit Name',
                }
            ),
            'image_url': forms.URLInput(
                attrs={
                    'placeholder': 'Fruit Image URL',
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Fruit Description',
                }
            ),
        }