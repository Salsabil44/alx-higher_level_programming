#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    for y in my_string:
        if y != "c" and y != "C":
            new_string += y
    return new_string
