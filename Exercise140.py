'''
In this exercise you will write a program that simulates a game of Bingo for a single
card. Begin by generating a list of all of the valid Bingo calls (B1 through O75). Once
the list has been created you can randomize the order of its elements by calling the
shufflefunction in therandommodule. Then your program should consume calls
out of the list, crossing out numbers on the card, until the card contains a crossed out
line (horizontal, vertical or diagonal). Simulate 1,000 games and report the minimum,
maximum and average number of calls that must be made before the card wins. Import
your solutions to Exercises 138 and 139 when completing this exercise.
'''

import random

def generate_bingo_card():
    bingo = {'B':[], 'I':[], 'N':[], 'G':[], 'O':[]}

    for _ in range(5):
        bingo['B'].append(str(random.randint(1, 15)))
        bingo['I'].append(str(random.randint(16, 30)))
        bingo['N'].append(str(random.randint(31, 45)))
        bingo['G'].append(str(random.randint(46, 60)))
        bingo['O'].append(str(random.randint(61, 75)))
    
    return bingo

def check_winning_line(bingo_card):
    for row in range(5):
        if all(bingo_card[col][row] == '0' for col in 'BINGO'):
            return True

    for col in 'BINGO':
        if all(bingo_card[col][row] == '0' for row in range(5)):
            return True

    if all(bingo_card['BINGO'[i]][i] == '0' for i in range(5)):
        return True
    if all(bingo_card['BINGO'[i]][4-i] == '0' for i in range(5)):
        return True

    return False

def simulate_bingo_game():
    bingo_card = generate_bingo_card()

    bingo_calls = [f'{letter}{number}' for letter in 'BINGO' for number in range(1, 76)]
    random.shuffle(bingo_calls)

    calls_made = 0

    for call in bingo_calls:
        calls_made += 1
        letter = call[0]
        number = call[1:]

        for i in range(5):
            if bingo_card[letter][i] == number:
                bingo_card[letter][i] = '0'
                break

        if check_winning_line(bingo_card):
            return calls_made

    return calls_made

def simulate_multiple_games(num_simulations):
    results = []

    for _ in range(num_simulations):
        calls_to_win = simulate_bingo_game()
        results.append(calls_to_win)

    min_calls = min(results)
    max_calls = max(results)
    average_calls = sum(results) / num_simulations

    print(f'Minimum calls to win: {min_calls}')
    print(f'Maximum calls to win: {max_calls}')
    print(f'Average calls to win: {average_calls:.2f}')

simulate_multiple_games(1000)
