import unittest
from source import Source


class SourceTest(unittest.TestCase):

    def test_successfully_create_source_with_monthly_only(self):
        channel = Source("Apartment Guide", 495)
        self.assertEqual(495, channel.monthly)

    def test_successfully_create_source_with_signed_lease_only(self):
        channel = Source("Apartments.com")
        channel.per_lease = 295
        self.assertEqual(295, channel.per_lease)

    def test_successfully_create_source_with_signed_lease_and_percentage_per_lease(self):
        channel = Source("Rent.com")
        channel.per_lease = 595
        channel.percentage_per_lease = 0.5
        self.assertEqual(595, channel.per_lease)
        self.assertEqual(0.5, channel.percentage_per_lease)

    def test_successfully_create_source_with_monthly_and_per_lead(self):
        channel = Source("Rent.com")
        channel.monthly = 195
        channel.per_lead = 25
        self.assertEqual(195, channel.monthly)
        self.assertEqual(25, channel.per_lead)

    def test_successfully_create_source_free(self):
        channel = Source("Craigslist")
        channel.free = True
        self.assertTrue(channel.free)
