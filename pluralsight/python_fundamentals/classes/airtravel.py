__author__ = 'ralph'

"""Model for aircraft flights"""

class Flight:
    """A flight with a particular passenger aircraft."""


    def __init__(self, number, aircraft):  # Accepts an aircraft object with class is constructed
        # String slicing used below
        # Also, logical negation operator 'not' used
        # Class Invariants are below
        if not number[:2].isalpha():
            raise ValueError("No airline code in '{}'".format(number))

        if not number[:2].isupper():
            raise ValueError("Invalid airline code in '{}'".format(number))

        if not number[2:].isdigit() and init(number[2:]) <= 9999:
            raise ValueError("Invalid route number '{}'".format(number))

        self._number = number
        self._aircraft = aircraft  # Accepts an aircraft object with class is constructed

    def number(self):
        return self._number

    def airline(self):
        return self._number[:2]

    # Following the Law of Demeter, method to return the aircraft model
    def aircraft_model(self):
        # This method delegates to aircraft through the client rather than
        # reaching through Flight and interrogate the aircraft directly
        return self._aircraft.model()



class Aircraft:
    # In production, we should validate as wells to that we can ensure
    # for example that the number of seats is NOT negative
    def __init__(self, registration, model, num_rows, num_seats_per_row):
        self._registration = registration
        self._model = model
        self._num_rows = num_rows
        self._num_seats_per_row = num_seats_per_row

    def registration(self):
        return self._registration

    def model(self):
        return self._model

    def seating_plan(self):
        # Added method which returns the allowed rows and seats as a tupl of range and seat letters
        return (range(1, self._num_rows + 1), # Range function produces an iterable series of row numbers up to the number in the plane
                "ABCDEFGHJK"[:self._num_seats_per_row]) # String and slice method return a string with one character per seat