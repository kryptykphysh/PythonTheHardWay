# ex4.py

#Total number of cars available.
cars = 100

# Capacity of a car to carry people.
space_in_a_car = 4.0

# Number of people able to drive cars.
drivers = 30

# Number of people needing to travel that cannot drive.
passengers = 90

# Bloody variable names TELL you what they are, but hey-ho
cars_not_driven = cars - drivers

cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven,"empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

# Q: I used 4.0 for space_in_a_car, but is that necessary? What happens 
# if it's just 4?
# Remember that 4.0 is a "floating point" number. Find out what 
# that means.

# A: It means calculations based on people will be able to return non-integer
# results. I'm not sure that's a good idea... could get messy.

# Q: Write comments above each of the variable assignments.

# Q: Make sure you know what = is called (equals) and that it's making 
# names for things.
# Remember _ is an underscore character.

# Q: Try running python as a calculator like you did before and use 
# variable names to do your calculations. Popular variable names are 
# also i, x, and j.