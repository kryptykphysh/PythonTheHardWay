# ex006.py

# Setting variable values to be interpolated in to strings.
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
# Interpolating variable values already set in to a string variable.
y = "Those who know %s and those who %s." % (binary, do_not)

# Outputting the strings created above.
print x
print y

# Interpolating the initial strings in to new strings and outpttuing them.
print "I said: %r." % x
print "I also said: '%s'." % y

# Setting a variable to the boolean value 'False'.
hilarious = False
# Creating a variable string that expects something to be interpolated.
joke_evaluation = "Isn't that joke so funny?! %r"

# Outputting the joke_avaluation string with the boolean variable interpolated.
print joke_evaluation % hilarious

# Setting more string variables.
w = "This is the left side of... "
e = "a string with a right side."

# Concatenating string variables and outputting.
print w + e

# Extra Credit

# Go through this program and write a comment above each line explaining it.

# Find all the places where a string is put inside a string. There are four places.
# Line 8 (twice), 15 and 16.

# Are you sure there's only four places? How do you know? Maybe I like lying.
# Pretty sure. the others are decimals or raw boolean.

# Explain why adding the two strings w and e with + makes a longer string.
# It's concatenation and it's what happens when you call the + method on a string.