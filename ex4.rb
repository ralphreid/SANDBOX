# sets car variable to 100
cars = 100
# sets space in cars
space_in_a_car = 4.0
# sets drivers
drivers = 30
# sets passengers to 90
passengers = 90
# calculates cars not driven
cars_not_driven = cars - drivers
# sets cars driven to num drivers
cars_driven = drivers
#calculates carpool capacity
carpool_capacity = cars_driven * space_in_a_car
#calculates average psg per car
average_passengers_per_car = passengers / cars_driven

puts "There are #{cars} cars available."
puts "There are only #{drivers} drivers available"
puts "There will be #{cars_not_driven} empty cars today."
puts "We can transport #{carpool_capacity} people today."
puts "We have #{passengers} passengers to carpool today."
puts "We need to put about #{average_passengers_per_car} in each car."