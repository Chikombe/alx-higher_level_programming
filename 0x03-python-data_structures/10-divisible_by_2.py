#!/usr/bin/python3
# 10-divisible_by_2.py

def divisible_by_2(my_list=[]):
    """Finds all multiples of two in a list."""
    multiples = []
    for itr in range(len(my_list)):
        if my_list[itr] % 2 == 0:
            multiples.append(True)
        else:
            multiples.append(False)

    return (multiples)
