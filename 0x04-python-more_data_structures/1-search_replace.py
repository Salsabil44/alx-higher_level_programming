#!/usr/bin/python3
def search_replace(my_list, search, replace):
    n_list = list(my_list)
    for y in range(len(n_list)):
        if n_list[y] == search:
            n_list[y] = replace
    return n_list
