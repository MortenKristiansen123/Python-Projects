import math  # math library
# String data type

# literal assignment
first = "Morten"
last = "Kristiansen"

# print(type(first))
# print(type(first) == str)
# print(isinstance(first, str))

# constructer function
# pizza = str("Pepperoni")
# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza, str))

# Concatenation
fullname = first + " " + last
print(fullname)

fullname += "!"
print(fullname)

# Casting a number to a string
decade = str(1996)
print(type(decade))
print(decade)

statement = "I like rock music from the " + decade + "s."
print(statement)

# Multiple lines
multiline = '''
Hey, how are you?                                           

I was just checking in.      
                                All good?

'''
print(multiline)

# Escaping special characters
sentence = 'I\'m back at work!\tHey!\n\nWhere\'s this at\\located?'
print(sentence)

# String Methods

print(first)
print(first.lower())
print(first.upper())
print(first)

print(multiline.title())
print(multiline.replace("good", "ok"))
print(multiline)

print(len(multiline))
multiline += "                                        "
multiline = "                         " + multiline
print(len(multiline))

print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))

print("")

# build a menu
title = "menu".upper()
print(title.center(27, "~"))
print("Coffee".ljust(22, ".") + "£1.50".rjust(4))
print("Muffin".ljust(22, ".") + "£2.50".rjust(4))
print("Cheesecake".ljust(22, ".") + "£4.50".rjust(4))

print("")

# string index values (0 represents the first character in an index)
print(first[0])
print(first[1])
print(first[-1])
print(first[1:-1])
print(first[1:])
print(first[0:])

print("")

# Some methods return boolean data
print(first.startswith("M"))
print(first.endswith("Z"))

# Boolen data type
myvalue = True
x = bool(False)
print(type(x))
print(isinstance(myvalue, bool))

# Numeric data type
# (Float is a function or reusable code in the Python programming language that converts values
# into floating point numbers. Floating point numbers are decimal values or fractional numbers
# like 133.5, 2897.11, and 3571.213, whereas real numbers like 56, 2, and 33 are called integers)

# integer
price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price, int))

# float type
gpa = 3.28
y = float(1.14)
print(type(gpa))
print(isinstance(y, float))

# complex type
comp_value = 5+3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

# built-in functions for numbers

print(abs(gpa))
print(abs(gpa * -1))

print(round(gpa))

print(round(gpa, 1))

print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))  # round up to nearest integer
print(math.floor(gpa))  # round down to nearest integer

# Casting a string to a number
zipcode = "10001"
zip_value = int(zipcode)
print(type(zip_value))

# Error if you attemt to cast incorrect data
# zip_value = int("New York") # commented out to avoid error

print("")
# Testing to see if it will say int instead of float when gpa was = 3.28
gpa = 3
print(type(gpa))

# Testing to see if its a str (string) or int (integer) as can be seen it is a string and if
# I wanted it to be an integer I would have to cast it to an int (integer) using the int() function
print("")
zipcode01 = "202"
print(type(zipcode01))
