'''
Write a program that begins by reading a temperature from the user in degrees
Celsius. Then your program should display the equivalent temperature in degrees
Fahrenheit and degrees Kelvin. The calculations needed to convert between different
units of temperature can be found on the internet.
'''

tempC = float(input('Temp in C: '))

tempF = (tempC * 9/5) + 32

tempK = tempC + 273.15

print(f'{tempC}°C is equal to {tempF}°F is equal to {tempK}°K.')