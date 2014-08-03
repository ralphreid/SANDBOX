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

  # setter methods
  def scan(item)
    @basket.push(item)
  end
  
  # instance method

  def self.count()
    @@count
  end

  def self.printCount()
    puts "Product count is : #@@count"
  end

end
