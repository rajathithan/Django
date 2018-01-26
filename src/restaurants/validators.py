from django.core.exceptions import ValidationError

categories=['mexican','asian','south indian','continental']

def category_validator(catvalue):
    catvaluecap = catvalue.lower()
    if not catvaluecap in categories :
        raise ValidationError("Not a valid Category")
