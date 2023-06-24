from django.db import models
from django.core.validators import MinLengthValidator
from .validators import first_name_validator



class Profile(models.Model):
    username = models.CharField(max_length=10, validators=[MinLengthValidator(2)])
    first_name = models.CharField(max_length=20, validators=[first_name_validator])
    last_name = models.CharField(max_length=20, validators=[first_name_validator])
    profile_picture = models.URLField(null=True, blank=True)

# Create your models here.
