'''
Using your solutions to Exercises 94 and 96, write a program that generates a random
good password and displays it. Count and display the number of attempts that were
needed before a good password was generated. Structure your solution so that it
imports the functions you wrote previously and then calls them from a function
named main in the file that you create for this exercise.
'''

import random

def randomPassword():
    length = random.randint(7, 10)
    password = ''.join(chr(random.randint(33, 126)) for _ in range(length))
    return password

def isGoodPassword(password):
    if len(password) < 8:
        return False
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    return has_upper and has_lower and has_digit

attempts = 0
while True:
    password = randomPassword()
    attempts += 1
    if isGoodPassword(password):
        print(f"Good password generated: {password}")
        break

print(f"Number of attempts: {attempts}")
