from django.db import models
from .validators import *
from django.core.validators import MinLengthValidator
from .validators import name_start_with_a_letter, fruit_name_consist_only_letter


class Profile(models.Model):
    first_name = models.CharField(verbose_name="First Name", max_length=25, validators=[MinLengthValidator(2), name_start_with_a_letter], blank=False, null=False)
    last_name = models.CharField(verbose_name="Last Name", blank=False, null=False, max_length=35, validators=[MinLengthValidator(1), name_start_with_a_letter])
    email = models.EmailField(verbose_name="Email", blank=False, null=False, max_length=40)
    password = models.CharField(verbose_name="Password", blank=False, null=False, max_length=20, validators=[MinLengthValidator(8)])
    image_url = models.URLField(verbose_name="Image URL", blank=True, null=True)
    age = models.IntegerField(verbose_name="Age", blank=True, null=True, default=18)


class Fruit(models.Model):
    name = models.CharField(verbose_name="Name", blank=False, null=False, max_length=30, validators=[MinLengthValidator(2), fruit_name_consist_only_letter])
    image_url = models.URLField(verbose_name="Image URL", blank=False, null=False)
    description = models.TextField(verbose_name="Description", blank=False, null=False)
    nutrition = models.TextField(verbose_name="Nutrition", blank=True, null=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
