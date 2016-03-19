class Project
  
  attr_accessor :name
  attr_reader :funding, :target

  def initialize(name, target_funding_amount, funding=0)
    @name = name
    @target = target_funding_amount
    @funding = funding
  end
  
  def to_s
    "#{@name} has $#{@funding} in funding towards a goal of $#{@target}." 
  end

  def remove_funds
    @funding -= 15
    puts "#{@name} lost some funds!"
  end
  
  def add_funds
    @funding += 25
    puts "#{@name} got more funds!"
  end
  
  def total_funding_outstanding
    @target - @funding
  end
end

project1 = Project.new("Project ABC", 5000, 1000)
puts project1

project2 = Project.new("Project LMN", 3000, 500)
puts project2

project3 = Project.new("Project XYZ", 75, 25)
puts project3

project4 = Project.new("Project TBD", 10000)
puts project4

puts "***"
puts project4.name
project4.name = "Project123"
puts project4.name
project1.remove_funds
project2.remove_funds
project3.add_funds
project4.add_funds
puts "***"

puts project1
puts project1.total_funding_outstanding
puts project2
puts project3
puts project4
