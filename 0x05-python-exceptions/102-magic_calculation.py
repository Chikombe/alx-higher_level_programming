#!/usr/bin/python3


def magic_calculation(a, b):
    ret_val = 0
    for itr in range(1, 3):
        try:
            if itr > a:
                raise Exception('Too far')
            else:
                ret_val += a ** b / itr
        except Exception as e:
            ret_val = b + a
            break
    return (ret_val)
