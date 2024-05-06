#!/usr/bin/python3
def remove_char_at(str, x):
    if x < 0:
        return str
    else:
        str = str[0:x] + str[x+1:]
    return str
