from django.core.exceptions import ValidationError


def year_of_car(value):
    if 1980 <= value <= 2049:
        pass
    else:
        raise ValidationError('Year must be between 1980 and 2049')