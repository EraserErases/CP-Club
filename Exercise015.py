"""
In this exercise, you will create a program that begins by reading a measurement
in feet from the user. Then your program should display the equivalent distance in
inches, yards and miles. Use the Internet to look up the necessary conversion factors
if you don't have them memorized.
"""

feets = float(input())

inches = feets * 12
yards = feets / 3
miles = feets / 5280

print(f'{feets} ft is equal to {inches} inches, {yards} yards and {miles} miles.')