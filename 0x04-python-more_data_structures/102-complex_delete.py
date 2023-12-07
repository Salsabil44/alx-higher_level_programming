#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    return {k: val for k, val in a_dictionary.items() if val != value}
