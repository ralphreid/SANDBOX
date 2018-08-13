class Stack:

    def __init__(self):
        self._items = []

    def is_empty(self):
        return not bool(self._items)

    def push(self, item):
        self._items.insert(0, item)

    def pop(self):
        return self._items.pop(0)

    def peek(self):
        return self._items[0]

    def size(self):
        return len(self._items)

# return a reversed copy of a list = 7,8,9 in & 9, 8, 7 out


def reverse(input_list):
    stack = Stack()

    for i in input_list:
        stack.push(i)

    tmp1 = Stack()
    while not stack.is_empty():
        tmp1.push(stack.pop())
    tmp2 = Stack()
    while not tmp1.is_empty():
        tmp2.push(tmp1.pop())
    while not tmp2.is_empty():
        stack.push(tmp2.pop())
    return tmp1

inputList = [7, 8, 9]

output = reverse(inputList)
print(output._items)



