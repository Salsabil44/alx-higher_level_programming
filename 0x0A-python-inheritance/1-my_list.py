#!/usr/bin/python3
"""class MyList th listt
"""


class MyList(list):
    """inherits from list"""
    def print_sorted(self):
        """prints the list, but sorted
        (ascending sort)
        """
        print(sorted(self))
