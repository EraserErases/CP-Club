'''
Write a program that reads an integer from the user. Then your program should
display a message indicating whether the integer is even or odd.
'''

num = int(input('Enter number: '))

print('Even') if num % 2 == 0 else print('Odd')