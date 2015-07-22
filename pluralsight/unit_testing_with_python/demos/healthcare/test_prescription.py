from datetime import date, timedelta

from prescription import Prescription

def days_ago(days):
    return date.today() - timedelta(days=days)

class TestPrescription:
    
    def test_days_taken_excludes_future_dates(self):
        prescription = Prescription("Codeine", dispense_date = days_ago(days=2), days_supply=4)
        assert prescription.days_taken() == [days_ago(2), days_ago(1)]
