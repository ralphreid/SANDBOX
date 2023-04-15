# use a recursive algorithm to find a maximum value


# declare a list of values to operate on
items = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]

def find_max(items):
    # breaking condition: last item in list? return it
    if len(items) == 1:
        return items[0]

    # otherwise get the first item and call function
    # again to operate on the rest of the list
    op1 = items[0]
    print(op1)
    op2 = find_max(items[1:])
    print(op1, op2)

    # perform the comparison when we're down to just two
    if op1 > op2:
        return op1
    else:
        return op2


# test the function
print(find_max(items))
# using a hashtable to count individual items


# define a set of items that we want to count
items = ["apple", "pear", "orange", "banana", "apple",
         "orange", "apple", "pear", "banana", "orange",
         "apple", "kiwi", "pear", "apple", "orange"]

# TODO: create a hashtable object to hold the items and counts
counter = None

# TODO: iterate over each item and increment the count for each one


# print the results
print(counter)
# use a recursive algorithm to find a maximum value


# declare a list of values to operate on
items = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]

def find_max(items):
    # TODO: breaking condition: last item in list? return it


    # TODO: otherwise get the first item and call function
    # again to operate on the rest of the list


    # TODO: perform the comparison when we're down to just two


# test the function
print(find_max(items))
# use a hashtable to filter out duplicate items


# define a set of items that we want to reduce duplicates
items = ["apple", "pear", "orange", "banana", "apple",
         "orange", "apple", "pear", "banana", "orange",
         "apple", "kiwi", "pear", "apple", "orange"]

# create a hashtable to perform a filter
filter = dict()

# loop over each item and add to the hashtable
for item in items:
    filter[item] = 0

# create a set from the resulting keys in the hashtable
result = set(filter.keys())
print(result)
# using a hashtable to count individual items


# define a set of items that we want to count
items = ["apple", "pear", "orange", "banana", "apple",
         "orange", "apple", "pear", "banana", "orange",
         "apple", "kiwi", "pear", "apple", "orange"]

# create a hashtable object to hold the items and counts
counter = dict()

# iterate over each item and increment the count for each one
for item in items:
    if item in counter.keys():
        counter[item] += 1
    else:
        counter[item] = 1

# print the results
print(counter)
# use a hashtable to filter out duplicate items


# define a set of items that we want to reduce duplicates
items = ["apple", "pear", "orange", "banana", "apple",
         "orange", "apple", "pear", "banana", "orange",
         "apple", "kiwi", "pear", "apple", "orange"]

# TODO: create a hashtable to perform a filter


# TODO: loop over each item and add to the hashtable


# TODO: create a set from the resulting keys in the hashtable
# try out the Python stack functions

# create a new empty stack
stack = []

# push items onto the stack
stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)

# print the stack contents
print(stack)

# pop an item off the stack LIFO
x = stack.pop()
print(x)
print(stack)
# try out the Python stack functions

# TODO: create a new empty stack


# TODO: push items onto the stack


# TODO: print the stack contents


# TODO: pop an item off the stack
# Linked list example


# the Node class
class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

    def get_data(self):
        return self.val

    def set_data(self, val):
        self.val = val

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next


# the LinkedList class
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        self.count = 0

    def get_count(self):
        return self.count

    def insert(self, data):
        # TODO: insert a new node
        new_node = Node(data)

    def find(self, val):
        # TODO: find the first item with a given value
        item = self.head

        return None

    def deleteAt(self, idx):
        # TODO: delete an item at given index
        if idx > self.count-1:
            return

    def dump_list(self):
        tempnode = self.head
        while (tempnode != None):
            print("Node: ", tempnode.get_data())
            tempnode = tempnode.get_next()


# create a linked list and insert some items
itemlist = LinkedList()
itemlist.insert(38)
itemlist.insert(49)
itemlist.insert(13)
itemlist.insert(15)
itemlist.dump_list()

# exercise the list
print("Item count: ", itemlist.get_count())
print("Finding item: ", itemlist.find(13))
print("Finding item: ", itemlist.find(78))

# delete an item
# itemlist.deleteAt(3)
# print("Item count: ", itemlist.get_count())
# print("Finding item: ", itemlist.find(38))
# itemlist.dump_list()
# Linked list example


# the Node class
class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

    def get_data(self):
        return self.val

    def set_data(self, val):
        self.val = val

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next


# the LinkedList class
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        self.count = 0

    def get_count(self):
        return self.count

    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node
        self.count += 1

    def find(self, val):
        item = self.head
        while (item != None):
            if item.get_data() == val:
                return item
            else:
                item = item.get_next()
        return None

    def deleteAt(self, idx):
        if idx > self.count:
            return
        if self.head == None:
            return
        else:
            tempIdx = 0
            node = self.head
            while tempIdx < idx-1:
                node = node.get_next()
                tempIdx += 1
            node.set_next(node.get_next().get_next())
            self.count -= 1

    def dump_list(self):
        tempnode = self.head
        while (tempnode != None):
            print("Node: ", tempnode.get_data())
            tempnode = tempnode.get_next()


# create a linked list and insert some items
itemlist = LinkedList()
itemlist.insert(38)
itemlist.insert(49)
itemlist.insert(13)
itemlist.insert(15)

itemlist.dump_list()

# exercise the list
print("Item count: ", itemlist.get_count())
print("Finding item: ", itemlist.find(13))
print("Finding item: ", itemlist.find(78))

# delete an item
itemlist.deleteAt(3)
print("Item count: ", itemlist.get_count())
print("Finding item: ", itemlist.find(38))
itemlist.dump_list()
# try out the Python queue functions
from collections import deque

# create a new empty deque object that will function as a queue
queue = deque()

# add some items to the queue
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)

# print the queue contents
print(queue)

# pop an item off the front of the queue
x = queue.popleft()
print(x)
print(queue)
# try out the Python queue functions


# TODO: create a new empty deque object that will function as a queue


# TODO: add some items to the queue


# TODO: print the queue contents


# TODO: pop an item off the front of the queue
# demonstrate hashtable usage


# TODO: create a hashtable all at once


# TODO: create a hashtable progressively


# TODO: try to access a nonexistent key


# TODO: replace an item


# TODO: iterate the keys and values in the dictionary
# demonstrate hashtable usage


# create a hashtable all at once
items1 = dict({"key1": 1, "key2": 2, "key3": "three"})
print(items1)


# create a hashtable progressively
items2 = {}
items2["key1"] = 1
items2["key2"] = 2
items2["key3"] = 3
print(items2)

# try to access a nonexistent key
# print(items1["key6"])

# replace an item
items2["key2"] = "two"
print(items2)

# iterate the keys and values in the dictionary
for key, value in items2.items():
    print("key: ", key, " value: ", value)
# Bubble sort algorithm


def bubbleSort(dataset):
    # start with the array length and decrement each time
    for i in range(len(dataset)-1, 0, -1):
        # examine each item pair
        for j in range(i):
            # swap items if needed
            if dataset[j] > dataset[j+1]:
                temp = dataset[j]
                dataset[j] = dataset[j+1]
                dataset[j+1] = temp

        print("Current state: ", dataset)


def main():
    list1 = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]
    print("Starting state: ", list1)
    bubbleSort(list1)
    print("Final state: ", list1)


if __name__ == "__main__":
    main()
# Bubble sort algorithm


def bubbleSort(dataset):
    # TODO: start with the array length and decrement each time

    print("Current state: ", dataset)


def main():
    list1 = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]
    bubbleSort(list1)
    print("Result: ", list1)


if __name__ == "__main__":
    main()
# Implement a quicksort


items = [20, 6, 8, 53, 56, 23, 87, 41, 49, 19]


def quickSort(dataset, first, last):
    if first < last:
        # calculate the split point
        pivotIdx = partition(dataset, first, last)

        # now sort the two partitions
        quickSort(dataset, first, pivotIdx-1)
        quickSort(dataset, pivotIdx+1, last)


def partition(datavalues, first, last):
    # choose the first item as the pivot value
    pivotvalue = datavalues[first]
    # establish the upper and lower indexes
    lower = first + 1
    upper = last

    # start searching for the crossing point
    done = False
    while not done:
        # TODO: advance the lower index

        # TODO: advance the upper index

        # TODO: if the two indexes cross, we have found the split point
        pass

    # when the split point is found, exchange the pivot value
    temp = datavalues[first]
    datavalues[first] = datavalues[upper]
    datavalues[upper] = temp

    # return the split point index
    return upper


# test the merge sort with data
print(items)
quickSort(items, 0, len(items)-1)
print(items)
# Implement a quicksort


items = [20, 6, 8, 53, 56, 23, 87, 41, 49, 19]


def quickSort(dataset, first, last):
    if first < last:
        # calculate the split point
        pivotIdx = partition(dataset, first, last)

        # now sort the two partitions
        quickSort(dataset, first, pivotIdx-1)
        quickSort(dataset, pivotIdx+1, last)


def partition(datavalues, first, last):
    # choose the first item as the pivot value
    pivotvalue = datavalues[first]
    # establish the upper and lower indexes
    lower = first + 1
    upper = last

    # start searching for the crossing point
    done = False
    while not done:
        # advance the lower index
        while lower <= upper and datavalues[lower] <= pivotvalue:
            lower += 1

        # advance the upper index
        while datavalues[upper] >= pivotvalue and upper >= lower:
            upper -= 1

        # if the two indexes cross, we have found the split point
        if upper < lower:
            done = True
        else:
            # exchange the two values
            temp = datavalues[lower]
            datavalues[lower] = datavalues[upper]
            datavalues[upper] = temp

    # when the split point is found, exchange the pivot value
    temp = datavalues[first]
    datavalues[first] = datavalues[upper]
    datavalues[upper] = temp

    # return the split point index
    return upper


# test the merge sort with data
print(items)
quickSort(items, 0, len(items)-1)
print(items)
# Implement a merge sort with recursion


items = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]

def mergesort(dataset):
    if len(dataset) > 1:
        mid = len(dataset) // 2
        leftarr = dataset[:mid]
        rightarr = dataset[mid:]

        # recursively break down the arrays
        mergeSort(leftarr)
        mergeSort(rightarr)

        # now perform the merging
        i=0 # index into the left array
        j=0 # index into the right array
        k=0 # index into merged array

        # while both arrays have content
        while i < len(leftarr) and j < len(rightarr):
            if leftarr[i] < rightarr[j]:
                dataset[k] = leftarr[i]
                i += 1
            else:
                dataset[k] = rightarr[j]
                j += 1
            k += 1

        # if the left array still has values, add them
        while i < len(leftarr):
            dataset[k] = leftarr[i]
            i += 1
            k += 1

        # if the right array still has values, add them
        while j < len(rightarr):
            dataset[k] = rightarr[j]
            j += 1
            k += 1


# test the merge sort with data
print(items)
mergesort(items)
print(items)
# Implement a merge sort with recursion


items = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]

def mergesort(dataset):
    if len(dataset) > 1:
        mid = len(dataset) // 2
        leftarr = dataset[:mid]
        rightarr = dataset[mid:]

        # TODO: recursively break down the arrays


        # TODO: now perform the merging
        i=0 # index into the left array
        j=0 # index into the right array
        k=0 # index into merged array

        # TODO: while both arrays have content


        # TODO: if the left array still has values, add them


        # TODO: if the right array still has values, add them



# test the merge sort with data
print(items)
mergesort(items)
print(items)
# Using recursion to implement power and factorial functions


def power(num, pwr):
    pass


def factorial(num):
    pass


print("{} to the power of {} is {}".format(5, 3, power(5, 3)))
print("{} to the power of {} is {}".format(1, 5, power(1, 5)))
print("{}! is {}".format(4, factorial(4)))
print("{}! is {}".format(0, factorial(0)))
# use recursion to implement a countdown counter


def countdown(x):
    return


countdown(5)
# Using recursion to implement power and factorial functions


def power(num, pwr):
    # breaking condition: if we reach zero, return 1
    if pwr == 0:
        return 1
    else:
        return num * power(num, pwr-1)


def factorial(num):
    if (num == 0):
        return 1
    else:
        return num * factorial(num-1)


print("{} to the power of {} is {}".format(5, 3, power(5, 3)))
print("{} to the power of {} is {}".format(1, 5, power(1, 5)))
print("{}! is {}".format(4, factorial(4)))
print("{}! is {}".format(0, factorial(0)))
# use recursion to implement a countdown counter


def countdown(x):
    if x == 0:
        print("Done!")
        return
    else:
        print(x, "...")
        countdown(x-1)


countdown(5)
# Find the greatest common denominator of two numbers
# using Euclid's algorithm


def gcd(a, b):
    while (b != 0):
        t = a       # set aside the value of a
        a = b       # set a equal to b
        b = t % b   # divide t (which is a) by b

    return a


# try out the function with a few examples
print(gcd(60, 96))  # should be 12
print(gcd(20, 8))   # should be 4
# Find the greatest common denominator of two numbers
# using Euclid's algorithm


def gcd(a, b):
    pass


# try out the function with a few examples
print(gcd(60, 96))  # should be 12
print(gcd(20, 8))   # should be 4
# determine if a list is sorted


items1 = [6, 8, 19, 20, 23, 41, 49, 53, 56, 87]
items2 = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]

def is_sorted(itemlist):
    # using the all function
    return all(itemlist[i] <= itemlist[i+1] for i in range(len(itemlist)-1))

    # using the brute force method
    # for i in range(0, len(itemlist)-1):
    #     if (itemlist[i] > itemlist[i+1]):
    #         return False
    # return True

print(is_sorted(items1))
print(is_sorted(items2))

# determine if a list is sorted


items1 = [6, 8, 19, 20, 23, 41, 49, 53, 56, 87]
items2 = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]

def is_sorted(itemlist):
    # TODO: using the brute force method

    return True

print(is_sorted(items1))
print(is_sorted(items2))

# searching for an item in an ordered list
# this technique uses a binary search


items = [6, 8, 19, 20, 23, 41, 49, 53, 56, 87]

def binarysearch(item, itemlist):
    # get the list size
    listsize = len(itemlist) - 1
    # start at the two ends of the list
    lowerIdx = 0
    upperIdx = listsize

    while lowerIdx <= upperIdx:
        pass
        # TODO: calculate the middle point


        # TODO: if item is found, return the index


        # TODO: otherwise get the next midpoint


    if lowerIdx > upperIdx:
        return None


print(binarysearch(23, items))
print(binarysearch(87, items))
print(binarysearch(250, items))
# searching for an item in an unordered list
# sometimes called a Linear search

# declare a list of values to operate on
items = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]

def find_item(item, itemlist):
    for i in range(0, len(itemlist)):
        if item == itemlist[i]:
            return i

    return None


print(find_item(87, items))
print(find_item(250, items))
# searching for an item in an ordered list
# this technique uses a binary search


items = [6, 8, 19, 20, 23, 41, 49, 53, 56, 87]

def binarysearch(item, itemlist):
    # get the list size
    listsize = len(itemlist) - 1
    # start at the two ends of the list
    lowerIdx = 0
    upperIdx = listsize

    while lowerIdx <= upperIdx:
        # calculate the middle point
        midPt = (lowerIdx + upperIdx)// 2

        # if item is found, return the index
        if itemlist[midPt] == item:
            return midPt
        # otherwise get the next midpoint
        if item > itemlist[midPt]:
            lowerIdx = midPt + 1
        else:
            upperIdx = midPt - 1

    if lowerIdx > upperIdx:
        return None


print(binarysearch(23, items))
print(binarysearch(87, items))
print(binarysearch(250, items))
# searching for an item in an unordered list
# sometimes called a Linear search

# declare a list of values to operate on
items = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]

def find_item(item, itemlist):
    pass


print(find_item(87, items))
print(find_item(250, items))
