'''
A triangle can be classified based on the lengths of its sides as equilateral, isosceles
or scalene. All 3 sides of an equilateral triangle have the same length. An isosceles
triangle has two sides that are the same length, and a third side that is a different
length. If all of the sides have different lengths then the triangle is scalene.
Write a program that reads the lengths of 3 sides of a triangle from the user.
Display a message indicating the type of the triangle.
'''

a = int(input('Side A: '))
b = int(input('Side B: '))
c = int(input('Side C: '))

if a == b == c:
    print('Equilateral Triangle')
elif a == b or a == c or c == b:
    print('Isosceles Triangle')
else:
    print('Scalene Triangle')