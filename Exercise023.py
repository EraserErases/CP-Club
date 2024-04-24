'''
A polygon is regular if its sides are all the same length and the angles between all of
the adjacent sides are equal. The area of a regular polygon can be computed using
the following formula, where s is the length of a side and n is the number of sides:
'''

import math

s = float(input('Length of a side: '))
n = int(input('# of sides: '))

area = (n * s ** 2) / 4 * math.tan(math.pi / n)

print(f'The area of the regular polygon is {area} units ^ 2.')