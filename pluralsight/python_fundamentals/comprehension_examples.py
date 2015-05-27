__author__ = 'ralph'


from math import factorial

# List comprehension example
f = [len(str(factorial(x))) for x in range(20)]
print(f)
print(type(f))

# Set comprehension example
f = {len(str(factorial(x))) for x in range(20)}
print(f)
print(type(f))

# Dictionary comprehension example
from pprint import pprint as pp

country_to_captial = {'United Kingdom': 'London',
                      'Brazil': 'Brazilia',
                      'Morocco': 'Rabat'}

# Unpacks using tuple unpacking to access the key and value separately
capital_to_country = {capital: country for country, capital in country_to_captial.items()}
pp(capital_to_country)