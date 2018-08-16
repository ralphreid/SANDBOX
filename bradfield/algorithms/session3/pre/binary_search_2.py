# Python Program for recursive binary search.

# Returns index of x in arr if present, else -1

def binary_search(arr, l, r, x):

    # Check base case
    if r >= l:

        mid = l + (r - l) // 2

        # If element is present at the middle itself
        if arr[mid] == x:
            return mid

        # If element is smaller than mid, then it
        # can only be present in left subarray
        elif arr[mid] > x:
            return binary_search(arr, l, mid - 1, x)

        # Else the element can only be present
        # in right subarray
        else:
            return binary_search(arr, mid + 1, r, x)

    else:
        # Element is not present in the array
        return -1

def report(result):
    if result:
        return print('dude')


# Test array
arr = [2, 3, 4, 10, 40]
x = 10

# Function call
result = binary_search(arr, 0, len(arr) - 1, x)

if result == -1:
    print
    "Element is not present in array"

else:
    print
    "Element is present at index %d" % result

print(result)
