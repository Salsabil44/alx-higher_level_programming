#!/usr/bin/python3
for num in range(9):
    for x in range(num + 1, 10):
        if num * 10 + x < 89:
            print("{:d}{:d}".format(num, x), end=", ")
print("{:d}".format(89))
