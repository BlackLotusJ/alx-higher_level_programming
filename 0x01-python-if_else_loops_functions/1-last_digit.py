i#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    lastdigit = number % -10
else:
    lastdigit = number % 10

if digit > 5:
    st = "and is greter than 5"
elif digit == 0:
    st = "and is 0"
else:
    st = "and is less than 6 and not 0"

print(f"Last digit of {number:d} is {lastdigit:d} {st}")
