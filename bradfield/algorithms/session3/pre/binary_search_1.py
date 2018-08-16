def binary_search(alist, item):
    if not alist:  # list is empty -- our base case
        return False

    midpoint = len(alist) // 2
    if alist[midpoint] == item:  # found it!
        return True

    if item < alist[midpoint]:  # item is in the first half, if at all
        return binary_search(alist[:midpoint], item)

    # otherwise item is in the second half, if at all
    return binary_search(alist[midpoint + 1:], item)


testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(binary_search(testlist, 3))  # => False
print(binary_search(testlist, 13))  # => True