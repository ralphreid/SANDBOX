__author__ = 'ralph'


def gen123():
    yield 1
    yield 2
    yield 3

# g = gen123()
#
# next(g)
# next(g)
# next(g)

for v in gen123():
    print(v)

def gen246():
    print("About to yield 2")
    yield 2
    print("About to yield 4")
    yield 4
    print("About to yield 6")
    yield 6
    print("About to return")

g = gen246()
