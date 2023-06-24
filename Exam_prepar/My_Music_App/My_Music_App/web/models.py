from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator
from .validators import username_validation, AlbumValidation, TextContainsOnlyAlphaNumericAndUnderscoreValidator


class Profile(models.Model):
    username = models.CharField(verbose_name="username", null=False, blank=False, max_length=15,
                                validators=[MinLengthValidator(2), TextContainsOnlyAlphaNumericAndUnderscoreValidator()])
    email = models.EmailField(verbose_name="email", blank=False, null=False)
    age = models.IntegerField(verbose_name="age", blank=True, null=True, validators=[MinValueValidator(0)])




    def __str__(self):
        return self.username


CHOICE_GENRE = (
    ("Pop Music", "Pop Music"),
    ("Jazz Music", "Jazz Music"),
    ("R&B Music", "R&B Music"),
    ("Rock Music", "Rock Music"),
    ("Country Music", "Country Music"),
    ("Dance Music", "Dance Music"),
    ("Hip Hop Music", "Hip Hop Music"),
    ("Other", "Other")
)


class Album(models.Model):
    album_name = models.CharField(verbose_name="album_name", unique=True, null=False, blank=False, max_length=30)
    artist = models.CharField(verbose_name="artist", null=False, blank=False, max_length=30)
    genre = models.CharField(verbose_name="genre", null=False, blank=False, max_length=30, choices=CHOICE_GENRE)
    description = models.TextField(verbose_name="description", blank=True, null=True)
    image_url = models.URLField(verbose_name="image_url", blank=False, null=False)
    price = models.FloatField(verbose_name="price", null=False, blank=False, validators=[MinValueValidator(0.0)])
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)