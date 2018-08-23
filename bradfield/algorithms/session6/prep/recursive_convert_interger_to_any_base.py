# overall algorithm will involve three components:
# #
# # Reduce the original number to a series of single-digit numbers.
# # Convert the single digit-number to a string using a lookup.
# # Concatenate the single-digit strings together to form the final result.


CHAR_FOR_INT = [0,1,2,3,4,5,6,7,8,9,'a','c','d','e','f']


def to_string(n, base):
    if n < base:
        return CHAR_FOR_INT[n]

    return to_string(n // base, base) + CHAR_FOR_INT[n % base]

to_string(1453, 16)  # => 5Ad