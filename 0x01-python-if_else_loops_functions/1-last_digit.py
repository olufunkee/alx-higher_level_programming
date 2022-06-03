#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_no = int(repr(number)[-1])
if (last_no > 5):
    print(f"Last digit of {number} is {last_no} and is greater than 5")
if (last_no == 0):
    print(f"Last digit of {number} is {last_no} and is 0")
else:
    print(f"Last digit of {number} is {last_no} and is less than 6 and not 0")
