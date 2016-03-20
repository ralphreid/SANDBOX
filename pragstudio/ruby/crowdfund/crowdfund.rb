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

class FundRequest
  
  attr_reader :title
  
  def initialize(title)
    @title = title
    @projects = []
  end
  
  def add_project(a_project)
    @projects.push(a_project)
  end
  
  def request_funding
    puts "There are #{@projects.size} projects that you could fund:"
    @projects.each do |project|
      puts project
    end
    @projects.each do |project|
      project.add_funds
      project.remove_funds
      project.add_funds
      puts project
    end
  end
end


project1 = Project.new("Project ABC", 5000, 1000)
project2 = Project.new("Project LMN", 3000, 500)
project3 = Project.new("Project XYZ", 75, 25)

projects = FundRequest.new("VC-Friendly Start-up Projects")
puts projects.title
projects.add_project(project1)
projects.add_project(project2)
projects.add_project(project3)
projects.request_funding

project4 = Project.new("Project TBD", 10000)

projectrequest = FundRequest.new("Ask My Family For Money")
puts projectrequest.title
projectrequest.add_project(project1)
projectrequest.add_project(project2)
projectrequest.add_project(project3)
projectrequest.add_project(project4)
projectrequest.request_funding
