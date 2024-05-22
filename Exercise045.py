'''
Write a program that reads a position from the user. Use an if statement to deter-
mine if the column begins with a black square or a white square. Then use modular

arithmetic to report the color of the square in that row. For example, if the user enters
a1 then your program should report that the square is black. If the user enters d5
then your program should report that the square is white. Your program may assume
that a valid position will always be entered. It does not need to perform any error
checking.
'''

letter = input('Enter the Letter: ').lower()
number = letter[1]


if letter[0] in ('a', 'c', 'e', 'g'):
    print('Black') if int(number) % 2 == 1 else print('White')
else:
    print('Black') if int(number) % 2 == 0 else print('White')