#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """A function that prints x elements of a list.

    Arguments:
        my_list (list): The list to print elements from.
        x (int): The number of elements of my_list to print.

    Returns:
        The real number of elements printed."""

    ret_val = 0
    for index in range(x):
        try:
            print("{}".format(my_list[index]), end="")
            ret_val += 1
        except IndexError:
            break
    print("")
    return (ret_val)
