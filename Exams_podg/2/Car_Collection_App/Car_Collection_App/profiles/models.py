from django.db import models

# Create your models here.
from .validators import username_minimum_length
from django.core.validators import MinLengthValidator

# Create your models here.


class Profile(models.Model):
    username = models.CharField(max_length=10, validators=[username_minimum_length])
    email = models.EmailField()
    age = models.IntegerField(MinLengthValidator(18))
    password = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    profile_picture = models.URLField(null=True, blank=True)