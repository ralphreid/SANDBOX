import unittest

from lead import Lead


class LeadTest(unittest.TestCase):
    def test_successfull_creation_of_a_lead(self):
        lead = Lead(1819343)
        self.assertTrue(lead)
