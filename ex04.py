# set cars (int) to 100
cars = 100
# set space_in_car (float) to 4.0
space_in_car = 4.0
# set drivers (int) and passengers (int) 
drivers = 30
passengers = 90
# cars_not_driven (int) is cars minus drivers
cars_not_driven = cars - drivers
#cars_driven (int) is drivers
cars_driven = drivers
#carpool_capacity (float) is cars_driven times space_in_car
carpool_capacity = cars_driven * space_in_car
#average_passengers is passengers divided by cars_driven
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
