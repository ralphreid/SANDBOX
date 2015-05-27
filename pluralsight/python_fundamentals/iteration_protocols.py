__author__ = 'ralph'

iterable = ['Spring', 'Summer', 'Autumn', 'Winter']

# iterator = iter(iterable)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))


# Here is a utility function
def first(iterable):
    iterator = iter(iterable)
    try:
        return next(iterator)
    except StopIteration:
        raise ValueError("iterable is empty")

print(first(["sasd", "2nd", "safdsafafsdfas"]))