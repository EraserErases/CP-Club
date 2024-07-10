'''
A standard deck of playing cards contains 52 cards. Each card has one of four suits
along with a value. The suits are normally spades, hearts, diamonds and clubs while
the values are 2 through 10, Jack, Queen, King and Ace.
Each playing card can be represented using two characters. The first character is
the value of the card, with the values 2 through 9 being represented directly. The
characters “T”, “J”, “Q”, “K” and “A” are used to represent the values 10, Jack,
Queen, King and Ace respectively. The second character is used to represent the suit
of the card. It is normally a lowercase letter: “s” for spades, “h” for hearts, “d” for
diamonds and “c” for clubs. The following table provides several examples of cards
and their two-character representations.
'''

import random

def createDeck():
    suits = ['s', 'h', 'd', 'c']
    values = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    deck = [value + suit for suit in suits for value in values]
    return deck

def shuffleDeck(deck):
    n = len(deck)
    for i in range(n):
        j = random.randint(0, n - 1)
        deck[i], deck[j] = deck[j], deck[i]

deck = createDeck()
print("Original deck:")
print(deck)

shuffleDeck(deck)
print("\nShuffled deck:")
print(deck)
