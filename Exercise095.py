'''
In a particular jurisdiction, older license plates consist of three letters followed by
three numbers. When all of the license plates following that pattern had been used,
the format was changed to four numbers followed by three letters.
Write a function that generates a random license plate. Your function should have
approximately equal odds of generating a sequence of characters for an old license
plate or a new license plate. Write a main program that calls your function and
displays the randomly generated license plate.
'''

import random
import string

def generateLicensePlate():
    if random.choice([True, False]):
        letters = ''.join(random.choices(string.ascii_uppercase, k=3))
        numbers = ''.join(random.choices(string.digits, k=3))
        return letters + numbers
    else:
        numbers = ''.join(random.choices(string.digits, k=4))
        letters = ''.join(random.choices(string.ascii_uppercase, k=3))
        return numbers + letters

print("Randomly generated license plate:", generateLicensePlate())
