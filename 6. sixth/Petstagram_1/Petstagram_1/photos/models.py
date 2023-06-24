from django.db import models
from django.core.validators import MinLengthValidator
from ..pets.models import Pet
from .validators import image_size_validator_5mb

# Create your models here.


class Photo(models.Model):
    pet_image = models.ImageField(blank=False,
                                  null=False,
                                  validators=(image_size_validator_5mb,),
                                  upload_to='..files/photos',
                                  )
    description = models.TextField(max_length=300,
                                   blank=True,
                                   null=True,
                                   validators=(MinLengthValidator(10),),
                                   )
    location = models.CharField(max_length=30, blank=True, null=True)
    tagged_pets = models.ManyToManyField(Pet, blank=True, null=True)
    date_of_publication = models.DateField(auto_now=True)