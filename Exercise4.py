"""
Create a program that reads the length and width of a farmer's field from the user in
feet. Display the area of the field in acres.
"""

length = float(input('Length of field in feet. '))
width = float(input('Length of width in feet. '))

area = (length * width) / 43560

print(f'With the inputed length {length} feet, and width {width}, the area of the field in acres is {area}.')