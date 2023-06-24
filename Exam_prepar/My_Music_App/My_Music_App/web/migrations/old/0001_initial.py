# Generated by Django 4.2.2 on 2023-06-21 12:49

import My_Music_App.web.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_name', models.CharField(max_length=30, unique=True, verbose_name='album_name')),
                ('artist', models.CharField(max_length=30, verbose_name='artist')),
                ('genre', models.CharField(choices=[('pop', 'Pop Music'), ('jazz', 'Jazz Music'), ('rnb', 'R&B Music'), ('rock', 'Rock Music'), ('country', 'Country Music'), ('dance', 'Dance Music'), ('hiphop', 'Hip Hop Music'), ('other', 'Other')], max_length=30, verbose_name='genre')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('image_url', models.URLField(verbose_name='image_url')),
                ('price', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='price')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=15, validators=[django.core.validators.MinLengthValidator(2), My_Music_App.web.validators.username_validation], verbose_name='username')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('age', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='age')),
            ],
        ),
    ]