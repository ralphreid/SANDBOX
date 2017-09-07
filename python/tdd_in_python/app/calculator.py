class Calculator(object):

    # def add(self, x, y):
    #     return x + y

    # REFACTORED for test 1
    def add(self, x, y):
        number_types = (int, float, complex)

        if isinstance(x, number_types) and isinstance(y, number_types):
            return x + y
        else:
            raise ValueError