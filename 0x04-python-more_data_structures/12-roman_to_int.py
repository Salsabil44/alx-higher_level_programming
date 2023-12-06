#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    r = 0
    p = 0
    
    for y in range(len(roman_string)-1, -1, -1):
        curr_value = roman_dict[roman_string[y]]
        
        if curr_value >= p:
            r += curr_value
        else:
            r -= curr_value
        
        p = curr_value
    
    return r
