cars = 100
space_in_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars-drivers
cars_driven = drivers
carpool_capacity = cars_driven*space_in_car
avg_pass_per_car = passengers/cars_driven

print "There are %d cars available!"% cars
print "There are only %d drivers here!"% drivers
