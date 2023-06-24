from django.core.exceptions import ValidationError
from django.core.validators import deconstructible

# def username_validation(value):
#     #letters, numbers, and underscore("_")
#     for i in value:
#         if i != "_" and not i.isalnum():
#             raise ValidationError("Ensure this value contains only letters, numbers, and underscore.")


@deconstructible
class username_validation:
    pass

@deconstructible
class TextContainsOnlyAlphaNumericAndUnderscoreValidator:
    def __call__(self, value):

        # char.isalnum() or char == '_' - returns True if char is alphanumeric or '_'
        # value.isalnum() and '_' not in value - wrong

        # regex: ^[a-zA-Z0-9_]+$ - ^ - start of string, $ - end of string
        # use in RegexValidator

        for char in value:
            if not (char.isalnum() or char == '_'):
                raise ValidationError('Ensure this value contains only letters, numbers, and underscore.')

    def __eq__(self, other):
        return True


class AlbumValidation:
    def __call__(self, value):
        if value < 0:
            raise ValidationError("Ensure this value is greater than or equal to 0.")


    def __eq__(self, other):
        return True