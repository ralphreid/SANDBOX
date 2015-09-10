import unittest

from leads import *


class LeadsTest(unittest.TestCase):
    def test_import_of_json(self):
        leads = Leads()
        self.assertTrue(leads.import_json())

