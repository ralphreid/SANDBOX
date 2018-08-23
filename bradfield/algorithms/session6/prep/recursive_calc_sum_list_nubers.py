# From https://bradfieldcs.com/algos/recursion/calculating-the-sum-of-a-list-of-numbers/

def iterative_sum(numbers):
    total = 0
    for n in numbers:
        total = total + n
    return total

iterative_sum([1, 3, 5, 7, 9])  # => 25

# This is an example of using recursion

def sum_of(numbers):
    if len(numbers) == 0:
        return 0

    return numbers[0] + sum_of(numbers[1:])

sum_of([1, 3, 5, 7, 9])  # => 25