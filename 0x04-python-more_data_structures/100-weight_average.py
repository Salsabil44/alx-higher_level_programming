#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    else:
        total = sum(a * b for a, b in my_list)
        total_w = sum(b for a, b in my_list)
        return total / total_w
