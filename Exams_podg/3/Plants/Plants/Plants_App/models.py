from django.db import models
from django.core.validators import MinLengthValidator
from .validators import validate_name_plant

PLANT_TYPE = (
    ('Outdoor Plants', 'Outdoor Plants'),
    ('Indoor Plants', 'Indoor Plants'),
)



class Plant(models.Model):
    plant_type = models.CharField(max_length=14, choices=PLANT_TYPE)
    name = models.CharField(max_length=20, validators=[MinLengthValidator(2), validate_name_plant])
    image_url = models.URLField()
    description = models.TextField()
    price = models.FloatField()

# Create your models here.
