#!/usr/bin/python3
import random
import math
Number = random.randint(-10000 , 10000)
mod =Number % 10 if Number >10 else Number %-10
print(
        "Last digit of {:d} is {:d} and is ".format(Number , mod) , end="")
if mod >5 :
    print ("greater than 5")
else if mod ==0 :
    print("0")
else:
    print("less than 6 and not 0")
