#!/usr/bin/python3
def safe_print_list(my_list=[], j=0):
    num = 0
    for y in range(j):
        try:
            print(my_list[y], end="")
            num += 1
        except IndexError:
            break
    print("")
    Return
