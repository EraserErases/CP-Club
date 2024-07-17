'''
Mathematical expressions are often written in infix form, where operators appear
between the operands on which they act. While this is a common form, it is also
possible to express mathematical expressions in postfix form, where the operator
appears after both operands. For example, the infix expression 3+4 is written as
34+ in postfix form. 
'''

def infixToPostfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    stack = []
    postfix = []

    for char in expression:
        if char.isnumeric():
            postfix.append(char)
        elif char in precedence:
            while (stack and stack[-1] != '(' and
                   precedence[stack[-1]] >= precedence[char]):
                postfix.append(stack.pop())
            stack.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()

    while stack:
        postfix.append(stack.pop())

    return ''.join(postfix)

expression = input("Enter an infix expression: ")
postfix = infixToPostfix(expression)
print("Postfix expression:", postfix)
