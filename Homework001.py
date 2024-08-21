'''
You're going to write an interactive calculator! User input is assumed to be a formula that consist of a number, an operator (at least + and -), and another number, separated by white space (e.g. 1 + 1). Split user input, and check whether the resulting list is valid:

If the input does not consist of 3 elements, raise a FormulaError, which is a custom Exception.
Try to convert the first and third input to a float. Catch any ValueError that occurs, and instead raise a FormulaError
If the second input is not '+' or '-', again raise a FormulaError
If the input is valid, perform the calculation and print out the result.
The user is then prompted to provide new input, and so on, until the user enters quit.
'''

class FormulaError(Exception):
    pass

def calculate(user_input):
    components = user_input.split()

    if len(components) != 3:
        raise FormulaError("Input does not consist of three elements")

    num1, operator, num2 = components

    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        raise FormulaError("The first and third input must be numbers")

    if operator not in ('+', '-'):
        raise FormulaError("The operator must be '+' or '-'")
    

    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2

while True:
    user_input = input("Enter a calculation (or type 'quit' to exit): ")
    if user_input.lower() == 'quit':
        break
    
    try:
        result = calculate(user_input)
        print("Result:", result)
    except FormulaError as e:
        print("Error:", e)

