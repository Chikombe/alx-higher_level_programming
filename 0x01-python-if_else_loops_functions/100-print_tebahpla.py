#!/usr/bin/python3
# 100-print_tebahpla.py

"""Prints the ASCII alphabet, in reverse order,
alternating lowercase and uppercase."""
itr = 0
for char in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(char - itr)), end="")
     itr = 32 if itr == 0 else 0
