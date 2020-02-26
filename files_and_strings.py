#!/usr/local/bin/python3

""" manipulating strings
 upper() - string property that makes all letters uppercase
 lower() - string property that makes all letters lowercase
 split() - string property that returns a list of strings separated by argument
 strip() - by default remotes white spaces from begining and end.
             look at lstrip and rstrip and arguments
"""

" letters ".upper()
" LeTteRs ".lower()
"a|delimited|string".split('|')
" a string with spaces   ".strip()

""" reading files
 with - creates a "context". keeps the file open while executing code "chunk"
 this is the idiomatic way, python is very idiomatic
"""

with open('filename.txt', 'r') as fh:
    line = fh.readline()
    while line:
        data = line.split(',')
        print(data[0])

""" reading files
 the less idiomatic way
 just an example of an alternative way, also to demonstrate why
"""
fh = open('filename.txt', 'r')
for line in fh.readlines():
    data = line.split(',')
    print(data[1])
fh.close()

