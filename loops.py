#!/usr/local/bin/python3

# https://www.tutorialsteacher.com/python/python-while-loop

""" while loops
 while some condition is true execute.
 often used for infinite loops while True
"""
i = 1
while i < 100:
    print("i is {}".format(i))
    i += 1

"""
 for loops
 iterates over some set of data
"""
l = [10, 20, 30, 40, 50]
for i in l:
    print(i)

d = {1:100, 2:200, 3:300}
for k,v in d.items():
    print("key =", k, ", value=",v)


# for loops and iterators
for i in range(1,4):
    for j in range(1,4):
        print("i:", i, " j:", j)
