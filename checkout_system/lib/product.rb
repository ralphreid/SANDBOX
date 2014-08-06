class Product
  # Initialize class variables
  @@count = 0

  attr_accessor :id, :name, :price, :discounted_price, :currency

  # constructor method
  def initialize(id, name, price, currency)
    # assign instance variables
    @id, @name, @price, @currency = id, name, price, currency
    @discounted_price = price

    @@count += 1
  end

  # accessor methods

  # setter methods

  # instance method

  def self.count()
    @@count
  end

  def self.printCount()
    puts "Product count is : #@@count"
  end

end
