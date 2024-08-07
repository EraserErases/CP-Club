'''
A Bingo card consists of 5 columns of 5 numbers. The columns are labeled with the
letters B, I, N, G and O. There are 15 numbers that can appear under each letter. In
particular, the numbers that can appear under the B range from 1 to 15, the numbers
that can appear under the I range from 16 to 30, the numbers that can appear under
the N range from 31 to 45, and so on.
Write a function that creates a random Bingo card and stores it in a dictionary. The
keys will be the letters B, I, N, G and O. The values will be the lists of five numbers
that appear under each letter. Write a second function that displays the Bingo card
with the columns labeled appropriately. Use these functions to write a program that
displays a random Bingo card. Ensure that the main program only runs when the file
containing your solution has not been imported into another program.
'''
import random

def generateBingo():
    bingo = {'B':[], 'I':[], 'N':[], 'G':[], 'O':[]}

    for _ in range(5):
        bingo['B'].append(str(random.randint(1, 15)))

    for _ in range(5):
        bingo['I'].append(str(random.randint(16, 30)))

    for _ in range(5):
        bingo['N'].append(str(random.randint(31, 45)))

    for _ in range(5):
        bingo['G'].append(str(random.randint(46, 60)))

    for _ in range(5):
        bingo['O'].append(str(random.randint(61, 75)))
    
    return bingo

def display(bingo):
    letters = 'BINGO'
    string = ''
    print('B\tI\tN\tG\tO')
    for _ in range(5):
        for j in range(5):
            string += bingo[letters[j]][_] + '\t'
        print(string)
        string = ''

display(generateBingo())