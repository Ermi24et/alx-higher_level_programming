#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number - (10 * int(number / 10))
less_than = "and is less than 6 and not 0"
equal_to = "and is 0"
greater = "and is greater than 5"
if last_digit < 6 and last_digit != 0:
    print(f"Last digit of {number} is {last_digit} {less_than}")
elif last_digit == 0:
    print(f"Last digit of {number} is {last_digit} {equal_to}")
else:
    print(f"Last digit of {number} is {last_digit} {greater}")
