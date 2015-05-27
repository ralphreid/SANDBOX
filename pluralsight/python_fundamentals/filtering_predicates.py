__author__ = 'ralph'

from math import sqrt

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


# filter applied to range
print([x for x in range(101) if is_prime(x)])

from pprint import pprint as pp

# Combining a filtering predicate with a transformation
# Dictionary transformation which maps numbers with three divisors
prime_square_divisors = {x*x:(1, x, x*x) for x in range(101)
                         if is_prime(x)}
pp(prime_square_divisors)