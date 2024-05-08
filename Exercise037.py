'''
Write a program that determines the name of a shape from its number of sides. Read
the number of sides from the user and then report the appropriate name as part of
a meaningful message. Your program should support shapes with anywhere from 3
up to (and including) 10 sides. If a number of sides outside of this range is entered
then your program should display an appropriate error message.
'''

sides = int(input('How many sides does your shape have: '))

shape = {
    3 : 'Triangle',
    4 : 'Square',
    5 : 'Pentagon',
    6 : 'Hexagon',
    7 : 'Heptagon',
    8 : 'Octagon',
    9 : 'Nonagon',
    10 : 'Decagon'
}

if sides in range(3, 11):
    print(f'The shape with sides {sides} is a "{shape[sides]}".')
else:
    print(f'You input of {sides} was invalid.')