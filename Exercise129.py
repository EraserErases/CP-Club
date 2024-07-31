'''
In this exercise you will simulate 1,000 rolls of two dice. Begin by writing a func-
tion that simulates rolling a pair of six-sided dice. Your function will not take any

parameters. It will return the total that was rolled on two dice as its only result.
Write a main program that uses your function to simulate rolling two six-sided
dice 1,000 times. As your program runs, it should count the number of times that each
total occurs. Then it should display a table that summarizes this data. Express the
frequency for each total as a percentage of the total number of rolls. Your program
should also display the percentage expected by probability theory for each total.
Sample output is shown below.
'''

import random

def rolltotal():
    roll1 = random.randint(1, 6)
    roll2 = random.randint(1, 6)
    return roll1 + roll2

count = {2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0}
percent = {2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0}
Expected = {2:2.78, 3:5.56, 4:8.33, 5:11.11, 6:13.89, 7:16.67, 8:13.89, 9:11.11, 10:8.33, 11:5.56, 12:2.78}

for _ in range(1000):
    roll = rolltotal()
    count[roll] += 1

for _ in range(2, 13):
    percent[_] = str(count[_] / 10) + '%'

print('Total\tSimulated\tExpected')

for _ in range(2, 13):
    print(f'{_}\t{percent[_]}\t\t{Expected[_]}%')