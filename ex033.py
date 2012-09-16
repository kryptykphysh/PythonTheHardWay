# ex033.py

from sys import argv

script, max_value, increment = argv

def loopy(exit_value, increment):
	i = 0
	numbers = []

	while i < exit_value:
		print "At the top i is %d" % i
		numbers.append(i)

		i += increment
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i

	print "The numbers: "

	for num in numbers:
		print num

loopy(int(max_value), int(increment))