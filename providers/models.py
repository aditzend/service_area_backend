from django.db import models


# TODO - Get a more comprehensive list of languages
LANGUAGE_CHOICES = sorted([
    ("EN", "English"), ("ES", "Spanish"), ("FR", "French")])

# TODO - Get a more comprehensive list of currencies
CURRENCY_CHOICES = sorted([
    ("USD", "US Dollars"), ("EUR", "Euros"), ("GBP", "Pounds")])


class Provider(models.Model):
    """
    A provider is a company that provides transportation services.
    """
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=True, default='')
    email = models.EmailField(max_length=254, blank=True, default='')
    phone_number = models.CharField(max_length=20, blank=True, default='')
    language = models.CharField(
        max_length=20, choices=LANGUAGE_CHOICES, default='English')
    currency = models.CharField(
        max_length=20, choices=CURRENCY_CHOICES, default='USD')

    class Meta:
        ordering = ['created']
