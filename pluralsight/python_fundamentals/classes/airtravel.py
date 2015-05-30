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

    def _parse_seat(self, seat):  # '_' used because this method is an implementation detail
        """Parse a seat designator into a valid row and letter.

        Args:
            seat: A seat designator such as 12F

        Returns:
            A tuple containing an integer and a string for row and seat.
        """
        row_numbers, seat_letters = self._aircraft.seating_plan()

        letter = seat[-1]  # Get seat letter through negative indexing into the seat string
        if letter not in seat_letters:
            raise ValueError("Invalid seat letter {}".format(letter))

        row_text = seat[:-1]  # Extract the row number by extracting all but the
        # # last character using string slicing
        try:
            row = int(row_text)  # Try to convert the row number substring to an int constructor
        except ValueError:
            # If that fails we catch the value error
            # Then the handler raises a new value valuable payload
            raise ValueError("Invalid seat row {}".format(row_text))

        if row not in row_numbers:  # Validate the row using an in operator against the rows range and this
            # is possible because range supports the container protocol
            raise ValueError("Invalid row number {}".format(row))

        return row, letter

    def allocate_seat(self, seat, passenger):
        """Allocate a seat to a passenger.

        Args:
            seat: A seat designator such as '12C' or '21F'
            passenger: The passenger name.

        Raises:
            ValueError: if the seat is unavailable.
        """
        # Notice method calls in the same object also require explicit qualification
        # the self prefix
        row, letter = self._parse_seat(seat)

        if self._seating[row][letter] is not None:
            raise ValueError("Seat {} already occupied".format(seat))

        self._seating[row][letter] = passenger

    def relocate_passenger(self, from_seat, to_seat):
        """Relocate a passenger to a different seat.

        Args:
            from_seat: The existing seat designator for the
                        passenger to be moved.

            to_seat: The new seat designator.
        """
        from_row, from_letter = self._parse_seat(from_seat)
        if self._seating[from_row][from_letter] is None:
            raise ValueError("No passenger to relocate in seat {}".format(from_seat))

        to_row, to_letter = self._parse_seat(to_seat)
        if self._seating[to_row][to_letter] is not None:
            raise ValueError("Seat {} is already occupied".format(to_seat))

        self._seating[to_row][to_letter] = self._seating[from_row][from_letter]
        self._seating[from_row][from_letter] = None

    def num_available_seats(self):
        # Achieved using TWO nested generator expressions
        # Outer expressions searches for all rows that are not none
        # which excludes our dummy first row
        # So the summ of this outer expression is the sum of values in each row
        # Inner expressions iterates over the dictionary and is the sum of None values in each row
        # Also, split the outer expression over three lines to improve readability
        # The inner expressions then adds ONE for each None seat found
        return sum(sum(1 for s in row.values() if s is None)
                   for row in self._seating
                   if row is not None)


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


# Convinience method so that I do not have to add flight and passengers every time
def make_flight():
    f = Flight("AA678", Aircraft("G-BRI", "Airbus A319", num_rows=24, num_seats_per_row=6))
    f.allocate_seat('12A', 'Bob Marlet')
    f.allocate_seat('15F', 'jah aha')
    f.allocate_seat('15E', 'Jane Smith')
    f.allocate_seat('1C', 'Caool Luke')
    f.allocate_seat('1D', 'Sam Smith')
    return f


# Follow the object oriented design principle;
# Rather than have a color printer query all of the passenger details,
# Follow this principal, 'Tell! Dont't Ask.' also related to law of demeter
# http://en.wikipedia.org/wiki/Law_of_Demeter
# Have the Flight TELL a simple Card Printing Function what to do
# This card printer is a module level function
# Notice the card printer does not know anything about flights or aircraft
# Its very loosely coupled,
def console_card_printer(passenger, seat, flight_number, aircraft):
    # Used 'line configuration' in the form of the '\' characters'
    # allows splitting of long characters over several lines
    output = "| Name:       {0}"      \
             "  Flight:     {1}"      \
             "  Seat:       {2}"      \
             "  Aircraft:   {3}"      \
             " |".format(passenger, flight_number, seat, aircraft)  # Implicit string concatenation
             # of adjacent strings to produce one long string with no line breaks
    # Measure length of the output line and build some banners and borders.
    banner = '+' + '-' * (len(output) - 2) + '+'
    border = '|' + ' ' * (len(output) - 2) + '|'
    lines = [banner, border, output, border, banner]  # construct a list of the elements
    card = 'n'.join(lines)  # Concatinate into a card
    print(card)  # print the whole card
    print()  # follow by a black line


# Interesting things:
# TypeError two positional argumetns could be caused by forgetting self in the  method