'''
Write a function that takes two positive integers that represent the numerator and
denominator of a fraction as its only two parameters. The body of the function
should reduce the fraction to lowest terms and then return both the numerator and
denominator of the reduced fraction as its result. For example, if the parameters
passed to the function are 6 and 63 then the function should return 2 and 21. Include
a main program that allows the user to enter a numerator and denominator. Then
your program should display the reduced fraction.
'''

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def reduceFraction(numerator, denominator):
    if denominator == 0:
        raise ValueError("Denominator cannot be zero.")
    common_divisor = gcd(numerator, denominator)
    return numerator // common_divisor, denominator // common_divisor

numerator = int(input("Enter the numerator: "))
denominator = int(input("Enter the denominator: "))

try:
    reduced_numerator, reduced_denominator = reduceFraction(numerator, denominator)
    print(f"The reduced fraction is: {reduced_numerator}/{reduced_denominator}")
except ValueError as e:
    print(e)
