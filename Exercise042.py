'''
In the previous question you converted from note name to frequency. In this question
you will write a program that reverses that process. Begin by reading a frequency
from the user. If the frequency is within one Hertz of a value listed in the table in
the previous question then report the name of the note. Otherwise report that the
frequency does not correspond to a known note. In this exercise you only need to
consider the notes listed in the table. There is no need to consider notes from other
octaves.

Note Frequency (Hz)
C4 261.63
D4 293.66
E4 329.63
F4 349.23
G4 392.00
A4 440.00
B4 493.88
'''

frequency = {
    261.63 : 'C4',
    293.66 : 'D4' ,
    329.63 : 'E4',
    349.23 : 'F4',
    392.00 : 'G4',
    440.00 : 'A4',
    493.88 : 'B4'
}

freq = float(input('Enter the frequency of the sound: '))

if freq in frequency:
    print(f'The note was {frequency[freq]}')
elif freq > 260.63 and freq < 262.63:
    print('The note was C4.')
elif freq > 292.66 and freq < 294.66:
    print('The note was D4.')
elif freq > 328.63 and freq < 330.63:
    print('The note was E4.')
elif freq > 348.23 and freq < 350.23:
    print('The note was F4.')
elif freq > 391.00 and freq < 393.00:
    print('The note was G4.')
elif freq > 439.00 and freq < 441.00:
    print('The note was A4.')
elif freq > 492.88 and freq < 494.88:
    print('The note was B4.')
else:
    print('There is no note of this frequency in memory.')