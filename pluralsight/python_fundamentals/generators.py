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