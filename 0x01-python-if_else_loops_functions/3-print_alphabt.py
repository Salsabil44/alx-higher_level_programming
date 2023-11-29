#!/usr/bin/python3
[200~output = ""
        for L in range(97, 123):
            char = chr(L)
                if char != 'q' and char != 'e':
                        output += char
                        print("{}".format(output), end="")
