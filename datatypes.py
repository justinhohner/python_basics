#!/usr/local/bin/python3

# https://www.tutorialsteacher.com/python/python-data-types
# 
"""
    Numeric
    Integer: Positive or negative whole numbers (without a fractional part)
    Float: Any real number with a floating point representation in which a fractional component is denoted by a decimal symbol or scientific notation

    Complex number: A number with a real and imaginary component represented as x+yj. x and y are floats and j is -1(square root of -1 called an imaginary number)
"""
x = 1
print(x)
y = 1.1
print(y)
j = -1
print(j)
i = x+j*y
print(i)

# Boolean
a = True
b = False
print(a)
print(b)

# String
a = "This is a string"
print(a)

# List
a = ["This", "is", "a", "list"]
print(a)
# Tuple
a = ("This", "is", "a", "list", 0)
print(a)
# Dictionary
a = {1:"Steve", 2:"Bill", 3:"Ram", 4: "Farha"}
print(a)
a = {"Steve":1, "Bill":2, "Ram":3, "Farha":4}
print(a)

"""
Create a variable to store your name and set it's value to your name
Create a list of numbers from 1 to 10
add the first 3 values of the list of numbers
"""