from django.core.exceptions import ValidationError



def profile_name_validator(value):
    l = [char for char in value]
    if not isupper(l[0]):
        raise ValidationError("Your name must start with a capital letter!")