'''
In this exercise you will create a program that reads a letter of the alphabet from the
user. If the user enters a, e, i, o or u then your program should display a message
indicating that the entered letter is a vowel. If the user enters y then your program
should display a message indicating that sometimes y is a vowel, and sometimes y is
a consonant. Otherwise your program should display a message indicating that the
letter is a consonant.
'''

letter = input('Enter a single letter: ')

if letter.isalpha() and len(letter) == 1:
    letter = letter.lower()
    if letter in ['a', 'e', 'i', 'o', 'u']:
        print('Vowel')
    elif letter == 'y':
        print('Sometimes a Vowl, Sometimes a Consonant')
    else:
        print('Consonant')
else:
    print('Invalid input')