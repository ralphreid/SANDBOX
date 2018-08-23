# https://bradfieldcs.com/algos/recursion/tower-of-hanoi/

# Move a tower of height-1 to an intermediate pole, using the final pole.
# Move the remaining disk to the final pole.
# Move the tower of height-1 from the intermediate pole to the final pole using the original pole.

# A tower of one disk will be our base case.


def move_tower(height, from_pole, to_pole, with_pole):
    if height >= 1:
        move_tower(height - 1, from_pole, with_pole, to_pole)
        move_disk(from_pole, to_pole)
        move_tower(height - 1, with_pole, to_pole, from_pole)

def move_disk(from_pole, to_pole):
    print('moving disk from {} to {}'.format(from_pole, to_pole))

move_tower(3,'A', 'B', 'C')

# moving disk from A to B
# moving disk from A to C
# moving disk from B to C
# moving disk from A to B
# moving disk from C to A
# moving disk from C to B
# moving disk from A to B