import unittest
from source import Source


class SourceTest(unittest.TestCase):

    def test_successfully_create_source_with_monthly_only(self):
        channel = Source("Apartment Guide", 495)
        self.assertEqual(495, channel.monthly)
