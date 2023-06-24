# Generated by Django 4.2.2 on 2023-06-23 10:27

import My_Music_App.web.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_album_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='username',
            field=models.CharField(max_length=15, validators=[django.core.validators.MinLengthValidator(2), My_Music_App.web.validators.TextContainsOnlyAlphaNumericAndUnderscoreValidator], verbose_name='username'),
        ),
    ]
