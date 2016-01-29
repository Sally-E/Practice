# -*-coding: utf-8-*-

import numpy as np

line1 = input('please enter numbers for first array: ').split(",")
line1 = list(map(int, line1))
print(line1)

line2 = input('please enter numbers for second array: ').split(",")
line2 = list(map(int, line2))
print(line2)

line1=np.array(line1)
line2=np.array(line2)


print (line1*line2)
