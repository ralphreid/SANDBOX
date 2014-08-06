class Checkout
  # Initialize class variables
  @@count = 0

  attr_accessor :basket
  # constructor method
  def initialize(rules)
    # assign instance variables
    @rules = rules
    @basket = []
    @@count += 1
  end

  # accessor methods
  def getBasket
    @basket
  end

  def total
    prices = []
    @basket.each {|e| prices.push(e.price)}
    prices.reduce(:+)
  end

  def discounted_total
    discounted_total = 0

    discounted_prices = []
    @basket.each {|e| discounted_prices.push(e.discounted_price)}
    discounted_total = discounted_prices.reduce(:+)

    @rules.each do |rule|
      if rule.item_id == nil
        discounted_total = rule.apply_discount_rule(discounted_total)
      end
    end

    return discounted_total
  end

  # setter methods
  def scan(item)
    @basket.push(item)

    @rules.each do |rule|
      unless rule.item_id == nil
        rule.apply_item_rule(@basket)
      end
    end
  end

  # instance method

  def self.count()
    @@count
  end

  def self.printCount()
    puts "Basket count is : #@@count"
  end

end
