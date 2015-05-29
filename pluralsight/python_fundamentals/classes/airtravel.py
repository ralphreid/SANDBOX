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

        # Receive the seating plan for the aircraft
        # Use tupl unpacking to put the row and seats into local variables
        rows, seats = self._aircraft.seating_plan()

        # Create a list for the seat allocations
        # [None] is a single entry list
        # used to waste one entry at the beginning of the list because row entries are
        # 1 based whereas python lists are 0 based
        # Use first entry to account for offset
        # Then concatenate one entry for each real row entry in the aircraft
        # _ used to discard the row numbers as we are not interested as it will match the final index
        # The item part of the list comprehension is {letter: None for letter in seats} which is a
        # dictionary comprehension which creates a mapping over each letter row to none indicating an empty seat
        # list comprehension [{letter: None for letter in seats} for _ in rows] used rather than list replication
        # with a multiplication operator because we want a distinct dictionary object created for each row

        self._seating = [None] + [{letter: None for letter in seats} for _ in rows]

    def number(self):
        return self._number

    def airline(self):
        return self._number[:2]

    # Following the Law of Demeter, method to return the aircraft model
    def aircraft_model(self):
        # This method delegates to aircraft through the client rather than
        # reaching through Flight and interrogate the aircraft directly
        return self._aircraft.model()

    def allocate_seat(self, seat, passenger):
        """Allocate a seat to a passenger.

        Args:
            seat: A seat designator such as '12C' or '21F'
            passenger: The passenger name.

        Raises:
            ValueError: if the seat is unavailable.
        """
        rows, seat_letters = self._aircraft.seating_plan()

        letter = seat[-1]  # Get seat letter through negative indexing into the seat string
        if letter not in seat_letters:
            raise ValueError("Invalid seat letter {}".format(letter))

        row_text = seat[:-1]  # Extract the row number by extracting all but the
        # last character using string slicing
        try:
            row = int(row_text)  # Try to convert the row number substring to an int constructor
        except ValueError:
            # If that fails we catch the value error
            # Then the handler raises a new value valuable payload
            raise ValueError("Invalid seat row {}".format(row_text))

        if row not in rows:  # Validate the row using an in operator against the rows range and this
            # is possible because range supports the container protocol
            raise ValueError("Invalid row number {}".format(row))

        # Check to see if seat is unoccupied using an identity test
        if self._seating[row][letter] is not None:
            raise ValueError("Seat {} already occupied".format(seat))

        self._seating[row][letter] = passenger


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


    # Examples of how to run access these classes and instantiate
    # f = Flight("BA456", Aircraft("G-RUT", "Airbus A320", num_rows=20, num_seats_per_row=5))
    # f.aircraft_model()