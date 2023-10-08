import pytest
from pytest_bdd import given, when, then, scenario

# Define the scenario(s)
@scenario('shopping_cart.feature', 'Add products to the shopping cart')
def test_shopping_cart():
    pass

# Fixture for the shopping cart
@pytest.fixture
def shopping_cart():
    return []

@given('I have an empty shopping cart')
def given_I_have_an_empty_shopping_cart(shopping_cart):
    assert len(shopping_cart) == 0

@when('I add "<product>" to the cart')
def when_I_add_product_to_the_cart(shopping_cart, product):
    shopping_cart.append(product)

@then('the cart should contain "<product>"')
def then_the_cart_should_contain_product(shopping_cart, product):
    assert product in shopping_cart
