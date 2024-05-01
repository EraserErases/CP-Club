'''
When the wind blows in cold weather, the air feels even colder than it actually is
because the movement of the air increases the rate of cooling for warm objects, like
people. This effect is known as wind chill.

In 2001, Canada, the United Kingdom and the United States adopted the fol-
lowing formula for computing the wind chill index. Within the formula Ta is the

air temperature in degrees Celsius and V is the wind speed in kilometers per hour.
A similar formula with different constant values can be used with temperatures in
degrees Fahrenheit and wind speeds in miles per hour.
'''

temp = float(input('Temp in C: '))
wind = float(input('Wind speed in k/hr: '))

WCI = 13.12 + 0.6215 * temp - 11.37 * wind ** 0.16 + 0.3965 * temp * wind ** 0.16

print(f'The value of the wind chill index is {WCI}')