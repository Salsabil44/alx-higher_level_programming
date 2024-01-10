#!/usr/bin/python3
import sys

def safe_function(f, *args):
    try:

        num = f(*args)
        return num
    except Exception as err:

        print("Exception: {}".format(err), file=sys.stderr)
        return None
