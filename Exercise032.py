'''
Create a program that reads three integers from the user and displays them in sorted
order (from smallest to largest). Use the min and max functions to find the smallest
and largest values. The middle value can be found by computing the sum of all three
values, and then subtracting the minimum value and the maximum value.
'''

numbers = [None] * 3

numbers[0] = int(input('Enter num1: '))
numbers[1] = int(input('Enter num2: '))
numbers[2] = int(input('Enter num3: '))

numbers.sort()

print(numbers)