from django.db import models
from django.core.validators import MinLengthValidator
from .validators import profile_first_name_validator

# Create your models here.

class Profile(models.Model):
    username = models.CharField(
        verbose_name='Username',
        max_length=10,
        validators=[
        MinLengthValidator(2),])
    
    first_name = models.CharField(
        max_length=20,
        validators=[
            profile_first_name_validator])

    last_name = models.CharField(
        max_length=20,
        validators=[
            profile_name_validator])

    profile_image_url = models.URLField(
        verbose_name="Picture URL")
