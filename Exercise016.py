'''
Write a program that begins by reading a radius, r, from the user. The program will
continue by computing and displaying the area of a circle with radius r and the
volume of a sphere with radius r. Use the pi constant in the math module in your
calculations.
'''

import math

r = int(input('Radius: '))

print(f'Area of the circle is {math.pi * r ** 2}, the volume of the sphere is {(4/3) * math.pi * r ** 3}')