#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_list = set(my_list)
    numb = 0

    for itr in uniq_list:
        numb += itr
    return (numb)
