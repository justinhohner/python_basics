#!/usr/local/bin/python3

# https://www.tutorialsteacher.com/python/python-user-defined-function

"""
  functions are an abstraction that make code easier to read and follow.
  breakg up code into discrete pieces of logic or functionality that are reusable
"""

"""
def function_name(parameters):
    "function docstring"
    statement1
    statement2
    ...
    ...
    return [expr]
"""

def f():
    "First line is docstring. When called, a message will be displayed"
    print ("Python functions are fun!")
    return

"""
 arguments
 functions take arguements as inputs and perform some action on them
 sometimes even return the results
 arguments to a function are a list by default. that means they are positional
"""
 
def f(x):
    "f of x returns x^2"
    return x**2

print(f(2))


"""
  lambdas! anonymous functions
  usuaully used one time, inline
"""

square = lambda x : x * x
print(square(5))

# more typical one time use from https://book.pythontips.com/en/latest/map_filter.html
number_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x < 0, number_list))
print(less_than_zero)
