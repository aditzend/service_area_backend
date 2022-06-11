from django.test import TestCase
from providers.models import Provider


class ProviderTestCase(TestCase):
    def setUp(self):
        Provider.objects.create(name="Provider 1", email="provider@one.com",
                                phone_number="+15468798755", language="EN",
                                currency="USD")
        Provider.objects.create(name="Provider 2", email="provider@two.com",
                                phone_number="+1546879874", language="ES",
                                currency="EUR")

    def test_provider_creation(self):
        """
        Test that a provider can be created.
        """
        provider1 = Provider.objects.get(name="Provider 1")
        provider2 = Provider.objects.get(name="Provider 2")
        self.assertEqual(provider1.name, "Provider 1")
        self.assertEqual(provider1.email, "provider@one.com")
        self.assertEqual(provider1.phone_number, "+15468798755")
        self.assertEqual(provider1.language, "EN")
        self.assertEqual(provider1.currency, "USD")
        self.assertEqual(provider2.name, "Provider 2")
        self.assertEqual(provider2.email, "provider@two.com")
        self.assertEqual(provider2.phone_number, "+1546879874")
        self.assertEqual(provider2.language, "ES")
        self.assertEqual(provider2.currency, "EUR")
