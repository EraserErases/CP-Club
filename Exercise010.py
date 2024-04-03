'''
Create a program that reads two integers, a and b, from the user. Your program should
compute and display:
• The sum of a and b
• The difference when b is subtracted from a
• The product of a and b
• The quotient when a is divided by b
• The remainder when a is divided by b
• The result of log10 a
• The result of a^b
'''

import math


a = int(input('Enter number a: '))
b = int(input('Enter number b: '))

sum = a + b
diff = a - b
prod = a * b
div = a / b
rem = a % b
log = math.log10(a)
expo = a ** b

print(f'The sum of a and b is {sum}. \nThe difference when b is subtracted from a is {diff}. \nThe product of a and b is {prod}. \nThe quotient when a is divided by b is {div}. \nThe remainder when a is divided by b is {rem}. \nThe Log10 of a is {log}. \nThe answer for a^b is {expo}.')