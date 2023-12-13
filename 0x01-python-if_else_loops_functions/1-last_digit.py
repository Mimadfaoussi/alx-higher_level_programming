#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
rest = number % 10
print(f"Last digit of {number} is {number % 10}",end='')
if (rest > 5):
    print("and is greater than 5")
elif (rest == 0):
    print("and is 0")
elif (rest < 6 and rest != 0):
    print(" and is less than 6 and not 0")
