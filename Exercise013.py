'''
Consider the software that runs on a self-checkout machine. One task that it must be
able to perform is to determine how much change to provide when the shopper pays
for a purchase with cash.
Write a program that begins by reading a number of cents from the user as an
integer. Then your program should compute and display the denominations of the
coins that should be used to give that amount of change to the shopper. The change
should be given using as few coins as possible. Assume that the machine is loaded
with pennies, nickels, dimes, quarters, loonies and toonies.
'''

cents = int(input())

if cents < 0:
    exit()

denominations = {
        'toonies': 200,
        'loonies': 100,
        'quarters': 25,
        'dimes': 10,
        'nickels': 5,
        'pennies': 1
    }

change = {}

for coin, value in denominations.items():
    num_coins = cents // value
    cents %= value
    if num_coins > 0:
        change[coin] = num_coins

print(change)