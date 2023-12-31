#!/usr/bin/python3
# 6-print_comb3.py

"""Print all possible different combinations of two digits in ascending order.
The two digits must be different - 01 and 10 are considered identical."""

for num1 in range(0, 10):
    for num2 in range(num1 + 1, 10):
        if num1 == 8 and num2 == 9:
            print("{}{}".format(num1, num2))
        else:
            print("{}{}".format(num1, num2), end=", ")
