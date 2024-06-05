'''
Write a function that takes three numbers as parameters, and returns the median value
of those parameters as its result. Include a main program that reads three values from
the user and displays their median.
'''

def medianOfThree(a, b, c):
    return sorted([a, b, c])[1]


print("Enter three numbers to find their median.")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

median = medianOfThree(num1, num2, num3)
print(f"The median of {num1}, {num2}, and {num3} is: {median}")
