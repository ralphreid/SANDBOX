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
project2 = Project.new("Project LMN", 3000, 500)
project3 = Project.new("Project XYZ", 75, 25)

projects = [project1, project2, project3]

puts "There are #{projects.size} projects that you could fund:"
projects.each do |project|
  puts project
end

puts "***"

puts "Here are the target funding amounts of each project:"
projects.each do |project|
  puts project.target
end

puts "***"

puts "Let's go through a round of funding requests and see what happens:"
projects.each do |project|
  project.add_funds
  project.remove_funds
  project.add_funds
  puts project
end

puts "***"

puts "Project ABC is removed and Project TBD is added. Now we have:"
projects.delete(project1)
project4 = Project.new("Project TBD", 10000)
projects.push(project4)
puts projects

