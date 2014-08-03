class Checkout
  # Initialize class variables
  @@count = 0

  attr_accessor :basket
  # constructor method
  def initialize()
    # assign instance variables
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

  # setter methods
  def scan(item)
    @basket.push(item)
  end

  # instance method

  def self.count()
    @@count
  end

  def self.printCount()
    puts "Basket count is : #@@count"
  end

end
