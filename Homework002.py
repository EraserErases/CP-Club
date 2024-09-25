def isBalanced(expression):
    stack = []
    brackets = {')': '(', '}': '{', ']': '['}  
    
    for char in expression:
        if char in '({[':  
            stack.append(char)
        elif char in ')}]':
            if not stack or stack[-1] != brackets[char]:
                return "Not Balanced"
            stack.pop() 
    

    return "Balanced" if not stack else "Not Balanced"

expression = input("Enter an expression with brackets to check if it's balanced: ")

result = isBalanced(expression)
print(f"Expression: {expression}, Result: {result}")