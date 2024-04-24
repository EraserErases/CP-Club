'''
In this exercise you will reverse the process described in the previous exercise.
Develop a program that begins by reading a number of seconds from the user.
Then your program should display the equivalent amount of time in the form

D:HH:MM:SS, where D, HH, MM, and SS represent days, hours, minutes and sec-
onds respectively. The hours, minutes and seconds should all be formatted so that

they occupy exactly two digits, with a leading 0 displayed if necessary.
'''

s = int(input('# of seconds: '))

time = {
        'D':86400,
        'H':3600,
        'M':60,
    }

finalTime = {}

for time, value in time.items():
    num_timeV = s // value
    s %= value
    if num_timeV > 0:
        finalTime[time] = num_timeV

print(f'{finalTime["D"]}:{finalTime["H"]:02}:{finalTime["M"]:02}:{s:02}')