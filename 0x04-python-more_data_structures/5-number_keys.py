#!/usr/bin/python3
def number_keys(a_dictionary):
    numb = 0
    list_keys = list(a_dictionary.keys())

    for itr in list_keys:
        numb += 1
    return (numb)
