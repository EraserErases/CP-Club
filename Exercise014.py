'''
Many people think about their height in feet and inches, even in some countries that
primarily use the metric system. Write a program that reads a number of feet from
the user, followed by a number of inches. Once these values are read, your program
should compute and display the equivalent number of centimeters.
'''

feets = float(input())
inches = float(input())

cm = (feets * 12 + inches) * 2.54

print(f'You are {cm}cm tall.')