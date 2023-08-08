#!usr/bin/python3
# 8-uppercase.py

def uppercase(input_str):
    """Print a string in uppercase."""
    for char in input_str:
        if ord(char) >= 97 and ord(char) <= 122:
            char = chr(ord(char) - 32)
        print("{}".format(char), end="")
    print("")
