__author__ = 'ralph'

A = [5, 5, 1, 7, 2, 3, 5]
_test = []
for value in A:
    if value == 5:
        _test.append(True)
    else:
        _test.append(False)

for i, val in enumerate(_test):
    if _test[:i].count(True) == _test[i:].count(False):
        print(i)
    elif _test[:i].count(False) == _test[i:].count(True):
        print(i)


_test[:4].count(True)

_test[4:].count(False)