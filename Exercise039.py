'''
Write a program that reads a sound level in decibels from the user. If the user
enters a decibel level that matches one of the noises in the table then your program
should display a message containing only that noise. If the user enters a number
of decibels between the noises listed then your program should display a message
indicating which noises the level is between. Ensure that your program also generates
reasonable output for a value smaller than the quietest noise in the table, and for a
value larger than the loudest noise in the table.
'''
import math

def roundup(num):
    return int(math.ceil(num/10.0)) * 10
def rounddown(num):
    return int(math.floor(num/10.0)) * 10

soundLevel = int(input('Sound level in dB: '))

soundChart = {
    0 : 'Softest Audible Sound',
    10 : 'Sound of breathing (self)',
    20 : 'Background noise in closed room',
    30 : 'Standing outside in nature (night)',
    40 : 'Quiet room',
    50 : 'The sound of the fridge',
    60 : 'Large office',
    70 : 'Alarm clock',
    80 : 'Vacuum Cleaner',
    90 : 'Standing next to the subway',
    100 : 'Standing next to factory machines',
    106 : 'Gas lawnmower',
    110 : 'Car horn from outside',
    120 : 'Police sirens',
    130 : 'Jackhammer',
    140 : 'Fighter jet take off'
}

if soundLevel in soundChart:
    print(f'The sound experienced is close to "{soundChart[soundLevel]}"')
elif soundLevel > 140:
    print('Number too big.')
elif soundLevel < 0:
    print('Number too small.')
else:
    print(f'The sound expericend is between "{soundChart[rounddown(soundLevel)]}" and "{soundChart[roundup(soundLevel)]}"')