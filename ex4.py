#total no of cars
cars = 100
#space in each car
space_in_a_car = 4.0
#no of drivers
drivers = 30
#no of passengers
passengers = 90
#cars which are going to be driven
cars_not_driven = cars - drivers
#exact no of cars which can be driven because of availibilty of drivers
cars_driven = drivers
#total no of persons which can actually travel 
carpool_capacity = cars_driven * space_in_a_car
#average passenger per car
average_passengers_per_car = passengers / cars_driven
print("there are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be:", cars_not_driven, "empty cars today.")
print("We can tranport", carpool_capacity, " people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car,"in each car.")