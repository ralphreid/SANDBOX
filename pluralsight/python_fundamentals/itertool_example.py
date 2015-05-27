__author__ = 'ralph'


from itertools import islice, count


from math import sqrt

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

thousand_primes = islice((x for x in count() if is_prime(x)), 1000)

list(thousand_primes)

# remember to pass it to the generator
sum(islice((x for x in count() if is_prime(x)), 1000))


any(is_prime(x) for x in range(1328, 1361))

all(name == name.title() for name in ['London', 'New York', 'Sydney'])


sunday  = [12, 13, 14, 15, 17]
monday  = [14, 45, 38, 23, 89]
tuesday = [2, 5, 7, 23, 45]

for item in zip(sunday, monday):
    print(item)

for sun, mon in zip(sunday, monday):
    print("average =", (sun + mon) / 2)

for temps in zip(sunday, monday, tuesday):
    print(("min={:4.1f}, max={:4.1f}, average={:4.1f}".format(
            min(temps), max(temps), sum(temps) / len(temps))))


from itertools import chain

temperatures = chain(sunday, monday, tuesday)

all(t > 0 for t in temperatures)