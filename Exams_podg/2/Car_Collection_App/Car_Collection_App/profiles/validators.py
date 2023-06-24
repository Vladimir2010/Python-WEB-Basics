from django.core.exceptions import ValidationError

def username_minimum_length(username):
    if len(username) >=2:
        pass
    else:
        raise ValidationError('The username must be a minimum of 2 chars')
