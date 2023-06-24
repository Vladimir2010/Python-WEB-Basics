from django.db import models
from django.utils.text import slugify

# Create your models here.


class Pet(models.Model):
    name = models.CharField(max_length=30)
    personal_photo = models.URLField()
    date_of_birth = models.DateField(blank=True, null=True)
    slg = models.SlugField(unique=True, blank=True, null=True)


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slg:
            self.slg = slugify(f"{self.name}-{self.pk}")
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.pk} - {self.name}"
