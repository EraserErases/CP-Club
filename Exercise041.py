'''
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
    'C4' : 261.63,
    'D4' : 293.66,
    'E4' : 329.63,
    'F4' : 349.23,
    'G4' : 392.00,
    'A4' : 440.00,
    'B4' : 493.88,
}

note = input('Enter a note between C4 and B4: ')

print(f'The frequency of the note was {frequency[note]}.') if note in frequency else print(f'The note {note} is not in memory. ')