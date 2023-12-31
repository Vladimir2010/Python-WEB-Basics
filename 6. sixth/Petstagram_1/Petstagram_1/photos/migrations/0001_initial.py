# Generated by Django 4.2.1 on 2023-06-06 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pets', '0002_alter_pet_slg'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pet_image', models.ImageField(upload_to='')),
                ('description', models.TextField(blank=True, max_length=300, null=True)),
                ('location', models.CharField(max_length=30)),
                ('date_of_publication', models.DateField(auto_now=True)),
                ('tagged_pets', models.ManyToManyField(blank=True, null=True, to='pets.pet')),
            ],
        ),
    ]
