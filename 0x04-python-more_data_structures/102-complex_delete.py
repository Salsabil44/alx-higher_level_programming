#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    return {ke: val for ke, val in a_dictionary.items() if val != value}
