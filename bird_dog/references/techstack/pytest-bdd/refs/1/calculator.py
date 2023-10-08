class Calculator:
    def __init__(self):
        self.value = 0

    def enter_number(self, number):
        self.value = number

    def press_add(self):
        self.value += self.value

    def press_multiply(self, number):
        self.value *= number

    def get_result(self):
        return self.value
