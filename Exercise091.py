'''
Write a function named precedence that returns an integer representing the prece-
dence of a mathematical operator. A string containing the operator will be passed to

the function as its only parameter. Your function should return 1 for + and -, 2 for *
and /, and 3 for ˆ. If the string passed to the function is not one of these operators
then the function should return -1. Include a main program that reads an operator

from the user and either displays the operator’s precedence or an error message indi-
cating that the input was not an operator. Your main program should only run when

the file containing your solution has not been imported into another program.
'''


operatorOrder = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
    '^': 3
}


operator = input("Enter a mathematical operator (+, -, *, /, ^): ")

if operator not in operatorOrder:
    print("Error: The input was not a valid operator.")
else:
    print(f"The precedence of the operator '{operator}' is: {operatorOrder[operator]}")

