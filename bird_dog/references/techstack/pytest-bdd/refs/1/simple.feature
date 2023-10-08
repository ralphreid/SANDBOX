from pytest_bdd import scenario, given, when, then

@scenario('calculator.feature', 'Addition')
def test_addition():
pass

@given("I have two numbers")
def step_given_numbers():
number1 = 5
number2 = 3
return number1, number2

@when("I add the numbers")
def step_when_add_numbers(step_given_numbers):
number1, number2 = step_given_numbers
result = number1 + number2
return result

@then("I should get the sum")
def step_then_sum(step_when_add_numbers):
assert step_when_add_numbers == 8
