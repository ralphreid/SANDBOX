Feature: Shopping Cart
  As a customer
  I want to add products to my shopping cart
  So that I can purchase them later

  Scenario Outline: Add products to the shopping cart
    Given I have an empty shopping cart
    When I add <product> to the cart
    Then the cart should contain <product>

    Examples:
      | product  |
      | Apples   |
      | Bananas  |
      | Oranges  |
