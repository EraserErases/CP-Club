'''
The volume of a cylinder can be computed by multiplying the area of its circular
base by its height. Write a program that reads the radius of the cylinder, along with
its height, from the user and computes its volume. Display the result rounded to one
decimal place.
'''
import math

r = int(input('Radius: '))
h = int(input('Height: '))

print(f'The volume of the cylinder is {round(math.pi * r ** 2 * h, 1)}')