'''
A univariate quadratic function has the form f (x) = ax2 + bx + c, where a, b and
c are constants, and a is non-zero. The roots of a quadratic function can be found
by finding the values of x that satisfy the quadratic equation ax2 + bx + c = 0. A
quadratic function may have 0, 1 or 2 real roots. These roots can be computed using
the quadratic formula, shown below:

root = (-b ± √(b^2 - 4ac)) / 2a

The portion of the expression under the square root sign is called the discriminant.
If the discriminant is negative then the quadratic equation does not have any real roots.
If the discriminant is 0, then the equation has one real root. Otherwise the equation
has two real roots, and the expression must be evaluated twice, once using a plus
sign, and once using a minus sign, when computing the numerator.
Write a program that computes the real roots of a quadratic function. Your program
should begin by prompting the user for the values of a, b and c. Then it should display
a message indicating the number of real roots, along with the values of the real roots
(if any).
'''

import math

def computeQuadraticRoots(a, b, c):
    discriminant = b**2 - 4*a*c
    
    if discriminant < 0:
        return 0, None
    elif discriminant == 0:
        root = -b / (2*a)
        return 1, (root,)
    else:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return 2, (root1, root2)


print("Welcome to the Quadratic Roots Finder!")

a = float(input("Please enter the value of a (non-zero): "))
if a == 0:
    print("The value of a must be non-zero. Please try again.")
    exit()

b = float(input("Please enter the value of b: "))
c = float(input("Please enter the value of c: "))

numRoots, roots = computeQuadraticRoots(a, b, c)

if numRoots == 0:
    print("The quadratic equation does not have any real roots.")
elif numRoots == 1:
    print(f"The quadratic equation has one real root: {roots[0]}")
else:
    print(f"The quadratic equation has two real roots: {roots[0]} and {roots[1]}")

