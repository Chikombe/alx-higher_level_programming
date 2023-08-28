#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """A function that prints the first x elements of a list and only integers.

    Areguments:
        my_list (list): The list to print elements from.
        x (int): The number of elements of my_list to print.

    Returns:
        The real number of integers printed."""

    ret_val = 0
    for index in range(0, x):
        try:
            print("{:d}".format(my_list[index]), end="")
            ret_val += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (ret_val)
