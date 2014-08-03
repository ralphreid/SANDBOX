class Checkout
  # Initialize class variables
  @@count = 0

  attr_accessor :id, :item

  # constructor method
  def initialize(id)
    # assign instance variables
    @id = id

    @@count += 1
  end

  # accessor methods
  def scan(item)
    puts item
  end
  # setter methods

  # instance method

  def self.count()
    @@count
  end

  def self.printCount()
    puts "Product count is : #@@count"
  end

end
