import pytest
from pytest_bdd import given, when, then, scenarios, parsers

# Define the scenario(s)
@scenarios('calculator.feature', example_converters=dict(number=int, result=int))
# Fixture for the calculator
@pytest.fixture
def calculator():
  return Calculator() # Assuming Calculator is a class that represents the calculator

Feature: Calculator
  As a user
  I want to use a calculator to add and multiply numbers
  So that I can save time doing math

  Scenario: Addition
  Given I have entered 50 into the calculator

# Step definitions
@given('I have entered <number> into the calculator')
def enter_number(calculator, number):
  calculator.enter_number(number)

@when('I press add')
def press_add(calculator):
  calculator.press_add()

@when(parsers.parse('I press multiply with {number:d}'))
def press_multiply(calculator, number):
  calculator.press_multiply(number)

@then('the result should be <result> on the screen')
def check_result(calculator, result):
  assert calculator.get_result() == result
    And I have entered 70 into the calculator
    When I press add
    Then the result should be 120 on the screen

  Scenario: Multiplication
    Given I have entered 5 into the calculator
    And I have entered 10 into the calculator
    When I press multiply with 2
    Then the result should be 20 on the screen
