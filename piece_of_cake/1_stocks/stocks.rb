require "test/unit"

# The indices are the time in minutes past trade opening time,
# which was 9:30am local time.
# So if the stock cost $500 at 10:30am, stock_prices_yesterday[60] = 500.
# Write an efficient function that takes stock_prices_yesterday and
# returns the best profit I could have made from 1 purchase
# and 1 sale of 1 Apple stock yesterday

stock_prices_yesterday = [10, 7, 5, 8, 11, 9]

class Calculator

  def initialize(stock_prices)
    @stock_price = stock_prices
  end

  def get_max_profit(stock_prices)

    return true
  end

end

# returns 6 (buying for $5 and selling for $11)
# def get_max_profit(stock_prices_yesterday)
#   # write the body of your function here
#   return "running with #{stock_prices_yesterday}"
# end
#
# puts get_max_profit('test input')


class TestCalculator < Test::Unit::TestCase
  def test_get_max_profit_raise_exception_when_stock_price_is_not_an_array_when_stock_price_is_not_an_array
    assert_
  end
end
