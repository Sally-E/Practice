# -*-coding: utf-8-*-

import sys

lines = sys.stdin.readlines()
print (lines)

for line in lines:
    if line.islower(): #if it is true, there are no capitals
        print (line, end="")
        print ('capital doesn\'t exist')

    else:
        print (line, end="")
        print ("capital exist")
