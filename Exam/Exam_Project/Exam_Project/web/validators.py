from django.core.exceptions import ValidationError


def name_start_with_a_letter(value):
    if not value[0].isalpha():
        raise ValidationError("Your name must start with a letter!")


def fruit_name_consist_only_letter(value):
    for i in value:
        if not i.isalpha():
            raise ValidationError("Fruit name should contain only letters!")