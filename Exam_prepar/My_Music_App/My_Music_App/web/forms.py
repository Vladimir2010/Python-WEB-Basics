from django import forms
from .models import Profile, Album


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'username': forms.TextInput(attrs={
                'placeholder': 'Username'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Email'
            }),
            'age': forms.NumberInput(attrs={
                'placeholder': 'Age'
            })
        }


class AlbumAdd(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'
        exclude = ['profile']
        widgets = {
            'album_name': forms.TextInput(attrs={
                'placeholder': 'Album Name'
            }),
            'artist': forms.TextInput(attrs={
                'placeholder': 'Artist'
            }),
            'genre': forms.Select(attrs={
                'placeholder': 'Genre'
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Description'
            }),
            'image_url': forms.URLInput(attrs={
                'placeholder': 'Image URL'
            }),
            'price': forms.NumberInput(attrs={
                'placeholder': 'Price'
            })
        }


# class EditAlbum(forms.ModelForm):
#     class Meta:
#         model = Album
#         fields = '__all__'
#         exclude = ['profile']
#         widgets = {
#             'album_name': forms.TextInput(attrs={
#                 'placeholder': Album.objects.get(id=id).album_name
#             }),
#             'artist': forms.TextInput(attrs={
#                 'placeholder': Album.objects.get(id=id).artist
#             }),
#             'genre': forms.Select(attrs={
#                 'placeholder': Album.objects.get(id=id).genre
#             }),
#             'description': forms.Textarea(attrs={
#                 'placeholder': Album.objects.get(id=id).description
#             }),
#             'image_url': forms.URLInput(attrs={
#                 'placeholder': Album.objects.get(id=id).image_url
#             }),
#             'price': forms.NumberInput(attrs={
#                 'placeholder': Album.objects.get(id=id).price
#             })
#         }

class DeleteAlbum(AlbumAdd):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs = {
                'readonly': 'readonly'
            }