'''
Write a program that allows the user to convert a number from one base to another.
Your program should support bases between 2 and 16 for both the input number and
the result number. If the user chooses a base outside of this range then an appropriate
error message should be displayed and the program should exit. Divide your program
into several functions, including a function that converts from an arbitrary base to
base 10, a function that converts from base 10 to an arbitrary base, and a main
program that reads the bases and input number from the user. You may find your
solutions to Exercises 77, 78 and 98 helpful when completing this exercise.
'''

def baseToDecimal(number, base):
    try:
        decimal = int(number, base)
        return decimal
    except ValueError:
        print(f"Error: '{number}' is not a valid number in base {base}.")
        exit(1)

def decimalToBase(decimal, base):
    if base < 2 or base > 16:
        print("Error: Base must be between 2 and 16.")
        exit(1)
    
    if decimal == 0:
        return '0'
    
    digits = "0123456789ABCDEF"
    result = ''
    
    while decimal > 0:
        remainder = decimal % base
        result = digits[remainder] + result
        decimal //= base
    
    return result


input_number = input("Enter the number to convert: ")
from_base = int(input("Enter the base of the input number (2-16): "))
to_base = int(input("Enter the base for the result number (2-16): "))

if from_base < 2 or from_base > 16 or to_base < 2 or to_base > 16:
    print("Error: Both bases must be between 2 and 16.")
    exit()

decimal_number = baseToDecimal(input_number, from_base)
result_number = decimalToBase(decimal_number, to_base)

print(f"{input_number} in base {from_base} is {result_number} in base {to_base}.")


