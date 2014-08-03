class Item
  # Initialize class variables
  @@count = 0

  # constructor method
  def initialize (product_code, name, price)
    # assign instance variables
    @product_code, @name, @price = product_code, name, price

    @@count += 1
  end

  # accessor methods

  # setter methods

  # instance method

  def self.printCount()
    puts "Item count is : #@@count"
 end

end
