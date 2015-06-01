__author__ = 'ralph'

import sys
from itertools import count, islice

# contains a generator for yielding the recman numbers
def sequence():
    """Generate Recaman's sequence."""
    seen = set()
    a = 0
    for n in count(1):
        yield a
        seen.add(a)
        c = a - n
        if c < 0 or c in seen:
            c = a + n
        a = c

# Writes the start of the sequence to a file
def write_sequence(filename, num):
    """Write Recaman's sequence to a pext file."""
    # with block means close is no longer needed explicitly
    with open(filename, mode='wt', encoding='utf-8') as f:
        # Generator function to covert the start of the sequence to a file
        # Generator expression used to convert each number to a string and add
        # a new line
        f.writelines("{0}\n".format(r)
                 for r in islice(sequence(), num + 1))  # islice used to truncate

if __name__ == '__main__':
    write_sequence(filename=sys.argv[1],
                   num=int(sys.argv[2]))