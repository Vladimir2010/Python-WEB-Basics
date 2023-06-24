from django.contrib import admin
from .models import Photo
from ..pets.models import Pet

# Register your models here.


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ("id", "date_of_publication", "description", "tagged_pets")


    @staticmethod
    def tagged_pets(self, obj):
        return ", ".join([Pet.name for pet in obj.tagged_pets.all()])
