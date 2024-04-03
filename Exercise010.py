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

print(f'\nThe sum of a and b is {sum}.\n'
    f'The difference when b is subtracted from a is {diff}. \n'
    f'The product of a and b is {prod}. \n'
    f'The quotient when a is divided by b is {div}. \n'
    f'The remainder when a is divided by b is {rem}. \n'
    f'The Log10 of a is {log}. \n'
    f'The answer for a^b is {expo}.')