'''
The amount of energy required to increase the temperature of one gram of a material
by one degree Celsius is the material's specific heat capacity, C. The total amount
of energy required to raise m grams of a material by ∆T degrees Celsius can be
computed using the formula:

q = mC∆T.

Write a program that reads the mass of some water and the temperature change
from the user. Your program should display the total amount of energy that must be
added or removed to achieve the desired temperature change.

Extend your program so that it also computes the cost of heating the water. Elec-
tricity is normally billed using units of kilowatt hours rather than Joules. In this

exercise, you should assume that electricity costs 8.9 cents per kilowatt-hour. Use
your program to compute the cost of boiling water for a cup of coffee.
'''

m  = float(input('Grams: '))
t = float(input('Temp Increase: '))

q = m * t * 4.186

c = q / 3600000  * 8.9

print(f'The amount of energy used is {q}, and the cost is {c} cents.')