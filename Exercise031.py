'''
Develop a program that reads a four-digit integer from the user and displays the sum
of the digits in the number. For example, if the user enters 3141 then your program
should display 3+1+4+1=9.
'''

num = input('Enter a 4 digit number: ')

if len(num) == 4:
    sum = int(num[0]) + int(num[1]) + int(num[2]) + int(num[3])
    print(f'{num[0]} + {num[1]} + {num[2]} + {num[3]} = {sum}')
else:
    print('Too long')