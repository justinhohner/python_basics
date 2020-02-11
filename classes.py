#!/usr/local/bin/python3

"""
  Python is an object oriented language that allows for additional abstraction.
  classes collection functions and variables into a single object that makes code easier to understand and use
"""

class Person(object):
    "Class doc strings go here."
    name = None
    age = 0
    parents = []

    def __init__(self, name, age, parents):
        self.name = name
        self.age = age
        self.parents = parents

    def introduce(self):
        print("Hello! My name is {}.".format(self.name))

    def add_parent(self, parent):
        self.paraents.append(parent)

morty_smith = Person('Morty Smith', 15, ['Jerry Smith', 'Beth Smith'])
morty_smith.introduce()
