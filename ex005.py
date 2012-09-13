# ex005.py
# -- coding: utf-8 -- 

name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
height_in_metric = height * 2.54 # centimenters
weight_in_metric = weight * 0.453592 #kilograms

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "Which is %r centimters." % height_in_metric
print "He's %d pounds heavy." % weight
print "That's %r kilograms." % weight_in_metric
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# This line is tricky, try to get it exactly right
print "If I add %d, %d and %d I get %d." % (age, height, weight,
	age + height + weight)

# Change all the variables so there isn't the my_ in front. 
# Make sure you change the name everywhere, not just where you used = to 
# set them.

# Try more format characters. %r is a very useful one. 
# It's like saying "print this no matter what".

# String and Unicode objects have one unique built-in operation: the % operator (modulo). This is also known as the string formatting or interpolation operator. Given format % values (where format is a string or Unicode object), % conversion specifications in format are replaced with zero or more elements of values. The effect is similar to the using sprintf() in the C language. If format is a Unicode object, or if any of the objects being converted using the %s conversion are Unicode objects, the result will also be a Unicode object.

# If format requires a single argument, values may be a single non-tuple object. [5] Otherwise, values must be a tuple with exactly the number of items specified by the format string, or a single mapping object (for example, a dictionary).

# A conversion specifier contains two or more characters and has the following components, which must occur in this order:

# The '%' character, which marks the start of the specifier.
# Mapping key (optional), consisting of a parenthesised sequence of characters (for example, (somename)).
# Conversion flags (optional), which affect the result of some conversion types.
# Minimum field width (optional). If specified as an '*' (asterisk), the actual width is read from the next element of the tuple in values, and the object to convert comes after the minimum field width and optional precision.
# Precision (optional), given as a '.' (dot) followed by the precision. If specified as '*' (an asterisk), the actual width is read from the next element of the tuple in values, and the value to convert comes after the precision.
# Length modifier (optional).
# Conversion type.
# When the right argument is a dictionary (or other mapping type), then the formats in the string must include a parenthesised mapping key into that dictionary inserted immediately after the '%' character. The mapping key selects the value to be formatted from the mapping. For example:

# >>>
# >>> print '%(language)s has %(number)03d quote types.' % \
# ...       {"language": "Python", "number": 2}
# Python has 002 quote types.
# In this case no * specifiers may occur in a format (since they require a sequential parameter list).

# The conversion flag characters are:

# Flag	Meaning
# '#'	The value conversion will use the “alternate form” (where defined below).
# '0'	The conversion will be zero padded for numeric values.
# '-'	The converted value is left adjusted (overrides the '0' conversion if both are given).
# ' '	(a space) A blank should be left before a positive number (or empty string) produced by a signed conversion.
# '+'	A sign character ('+' or '-') will precede the conversion (overrides a “space” flag).
# A length modifier (h, l, or L) may be present, but is ignored as it is not necessary for Python – so e.g. %ld is identical to %d.

# The conversion types are:

# Conversion	Meaning	Notes
# 'd'	Signed integer decimal.	 
# 'i'	Signed integer decimal.	 
# 'o'	Signed octal value.	(1)
# 'u'	Obsolete type – it is identical to 'd'.	(7)
# 'x'	Signed hexadecimal (lowercase).	(2)
# 'X'	Signed hexadecimal (uppercase).	(2)
# 'e'	Floating point exponential format (lowercase).	(3)
# 'E'	Floating point exponential format (uppercase).	(3)
# 'f'	Floating point decimal format.	(3)
# 'F'	Floating point decimal format.	(3)
# 'g'	Floating point format. Uses lowercase exponential format if exponent is less than -4 or not less than precision, decimal format otherwise.	(4)
# 'G'	Floating point format. Uses uppercase exponential format if exponent is less than -4 or not less than precision, decimal format otherwise.	(4)
# 'c'	Single character (accepts integer or single character string).	 
# 'r'	String (converts any Python object using repr()).	(5)
# 's'	String (converts any Python object using str()).	(6)
# '%'	No argument is converted, results in a '%' character in the result.	 

# Search online for all of the Python format characters.

# Try to write some variables that convert the inches and 
# pounds to centimeters and kilos. Do not just type in the 
# measurements. Work out the math in Python.