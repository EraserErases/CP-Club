'''
Create a program that reads a duration from the user as a number of days, hours,
minutes, and seconds. Compute and display the total number of seconds represented
by this duration.
'''

d = int(input('# of days: '))
h = int(input('# of hours: '))
m = int(input('# of minutes: '))
s = int(input('# of seconds: '))

totalS = ((d * 24 + h) * 60 + m) * 60 + s

print(f'The time entered converted into seconds is {totalS} seconds.')