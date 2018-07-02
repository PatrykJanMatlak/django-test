from django.core.exceptions import ValidationError

CATEGORIES = ['Italian','Pizza','American','Other', 'Polish']

def validate_category(value):
    cat = value.capitalize()
    if not value in CATEGORIES and not cat in CATEGORIES:
        raise ValidationError(f'{value} is not in categories!',
        params = {'value' : value}) 