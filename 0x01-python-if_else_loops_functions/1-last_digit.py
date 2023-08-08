#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = abs(number) % 10
if number < 0:
    digit = -digit
message = ("Last digit of {} is {} and is".format(number, digit), end="")
if digit > 5:
    print(message,"greater than 5")
elif digit == 0:
    print(message,"0")
else:
    print(message,"less than 6 and not 0")
