#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    my_dict = dict(a_dictionary)
    for k, i in my_dict.items():
        my_dict[k] = i * 2
    return my_dict
