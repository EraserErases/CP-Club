'''
In the previous exercise you created a program that computed the area of a triangle
when the length of its base and its height were known. It is also possible to compute
the area of a triangle when the lengths of all three sides are known. Let s1, s2 and s3
be the lengths of the sides. Let s = (s1 + s2 + s3)/2. Then the area of the triangle
can be calculated using the following formula:
'''

s1 = float(input('Side1: '))
s2 = float(input('Side2: '))
s3 = float(input('Side3: '))

s = (s1 + s2 + s3) / 2

print(f'The area of the triangle is {round((s * (s - s1) * (s - s2) * (s - s3) * .5), 2)}')

