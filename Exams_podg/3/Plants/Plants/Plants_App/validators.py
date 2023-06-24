from django.core.exceptions import ValidationError


def validate_name_plant(value):
    for letter in value:
        if not letter.isalpha():
            raise ValidationError('Plant name should contain only letters!')
