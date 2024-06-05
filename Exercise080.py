'''
What’s the minimum number of times you have to flip a coin before you can have
three consecutive flips that result in the same outcome (either all three are heads or
all three are tails)? What’s the maximum number of flips that might be needed? How
many flips are needed on average? In this exercise we will explore these questions
by creating a program that simulates several series of coin flips.
Create a program that uses Python’s random number generator to simulate flipping
a coin several times. The simulated coin should be fair, meaning that the probability
of heads is equal to the probability of tails. Your program should flip simulated
coins until either 3 consecutive heads of 3 consecutive tails occur. Display an H each
time the outcome is heads, and a T each time the outcome is tails, with all of the
outcomes shown on the same line. Then display the number of flips needed to reach
3 consecutive flips with the same outcome. When your program is run it should
perform the simulation 10 times and report the average number of flips needed.
Sample output is shown below:
'''
import random

count = 0

def simulatedFlips():
    flips = ''
    prev2Flip = ''
    prev1Flip = ''
    curflip = ''
    global count
    count = 0
    while True:
        curflip = random.choice(['H ', 'T '])
        count += 1

        flips += curflip
        "HHHH" in flips or TTT
        if prev1Flip == prev2Flip == curflip:
            return flips + f'({count} flips)'
        
        prev2Flip = prev1Flip
        prev1Flip = curflip

sum = 0

for _ in range(10):
    print(simulatedFlips())
    sum += count

print(f'On average, {sum / 10} flips were needed.')