__author__ = 'ralph'

"""Model for aircraft flights"""

class Flight:

    def __init__(self, number):
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

    def number(self):
        return self._number

    def airline(self):
        return self._number[:2]


class Aircraft:
    # In production, we should validate as wells to that we can ensure
    # for example that the number of seats is NOT negative
    def __init__(self, registration, model, num_rows, num_seats_per_row):
        self._registration = registration
        self._model = model
        self._num_rows = num_rows
        self._num_seats_per_row

    def registration(self):
        return self._registration

    def model(self):
        return self._model