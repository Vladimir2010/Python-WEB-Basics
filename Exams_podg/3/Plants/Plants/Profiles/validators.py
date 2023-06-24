from django.core.exceptions import ValidationError

def first_name_validator(value):
    if value[0].isupper():
        pass
    else:
        raise ValidationError("Your name must start with a capital letter!")