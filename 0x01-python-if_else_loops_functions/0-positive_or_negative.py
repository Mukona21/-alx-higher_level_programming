#!/usr/bin/python3
import random
number = random.randint(-10, 10)  # Generate a random number between -10 and 10 (inclusive)

if number > 0:
    print(number, "is positive")
elif number == 0:
    print(number, "is zero")
else:
    print(number, "is negative")