#!/usr/bin/python3


class LockedClass:
    

    def __setattr__(self, name, value):
        
        if name != "first_name":
            raise AttributeError("'LockedClass' object has no attribute '" +
                                 name + "'")

    def __getattribute__(self, name):
        
        if name == "__dict__":
            raise AttributeError("'LockedClass' object has no attribute '" +
                                 name + "'")
