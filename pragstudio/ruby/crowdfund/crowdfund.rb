def time
	  current_time = Time.new
	    current_time.strftime("%A, %B %d, %Y")
end

def project_listing(name, funding=0)
	  "#{name} has $#{funding} in funding as of #{time}."
end

puts project_listing("Project ABC", 1000)
puts project_listing("Project LMN", 500)
puts project_listing("Project XYZ", 25)
puts project_listing("Project TBD")

