'''
Create a program that reads integers from the user until a blank line is entered. Once
all of the integers have been read your program should display all of the negative
numbers, followed by all of the zeros, followed by all of the positive numbers. Within
each group the numbers should be displayed in the same order that they were entered
by the user. For example, if the user enters the values 3, -4, 1, 0, -1, 0, and -2 then
your program should output the values -4, -1, -2, 0, 0, 3, and 1. Your program
should display each value on its own line.
'''

negative_numbers = []
zeros = []
positive_numbers = []

print("Enter integers (blank line to stop):")

while True:
    user_input = input()

    if user_input == "":
        break

    number = int(user_input)
    
    if number < 0:
        negative_numbers.append(number)
    elif number == 0:
        zeros.append(number)
    else:
        positive_numbers.append(number)

for number in negative_numbers:
    print(number)
for number in zeros:
    print(number)
for number in positive_numbers:
    print(number)
