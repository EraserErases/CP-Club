'''
If you have 3 straws, possibly of differing lengths, it may or may not be possible
to lay them down so that they form a triangle when their ends are touching. For
example, if all of the straws have a length of 6 inches. then one can easily construct
an equilateral triangle using them. However, if one straw is 6 inches. long, while the
other two are each only 2 inches. long, then a triangle cannot be formed. In general,
if any one length is greater than or equal to the sum of the other two then the lengths
cannot be used to form a triangle. Otherwise they can form a triangle.
Write a function that determines whether or not three lengths can form a triangle.
The function will take 3 parameters and return a Boolean result. In addition, write a
program that reads 3 lengths from the user and demonstrates the behaviour of this
function.
'''

def canFormTriangle(a, b, c):
    return a + b > c and a + c > b and b + c > a


print("Enter the lengths of three straws.")

a = float(input("Enter the length of the first straw: "))
b = float(input("Enter the length of the second straw: "))
c = float(input("Enter the length of the third straw: "))

if canFormTriangle(a, b, c):
    print(f"The lengths {a}, {b}, and {c} can form a triangle.")
else:
    print(f"The lengths {a}, {b}, and {c} cannot form a triangle.")
