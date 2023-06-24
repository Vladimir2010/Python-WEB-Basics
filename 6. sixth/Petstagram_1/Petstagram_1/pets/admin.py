from django.contrib import admin
from .models import Pet

# Register your models here.

@admin.register(Pet)
class Pet_Admin(admin.ModelAdmin):
    list_display = ('name', 'slg')