from django.db import models
from .validators import *
from django.core.validators import MinLengthValidator

type_cars = (
    ('Sports Car', 'Sports Car'),
    ('Pickup', 'Pickup'),
    ('Crossover', 'Crossover'),
    ('Minibus', 'Minibus'),
    ('Other', 'Other'),
)


class Car(models.Model):
    type = models.CharField(max_length=10, choices=type_cars)
    model = models.CharField(max_length=20, validators=[MinLengthValidator(2)])
    year = models.IntegerField()
    image_url = models.URLField()
    price = models.FloatField(validators=[MinLengthValidator(1)])


