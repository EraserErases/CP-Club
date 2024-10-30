'''
#1 Write a program and recurrence relation to find the Fibonacci series of n where n>2 .
Mathematical Equation:

n if n == 0, n == 1;

fib(n) = fib(n-1) + fib(n-2) otherwise;

Sample:

Input: n = 5

Output:

Fibonacci series of 5 numbers is : 0 1 1 2 3
'''

rep = int(input('Number of Repitions: '))

FibNum = [0, 1]
output = ''

if rep < 2:
    print('Input Number too small.')
    exit()

for _ in range(rep - 2):
    FibNum.append(FibNum[_] + FibNum[_ + 1])

for _ in range(len(FibNum)):
    output += str(FibNum[_]) + ' '


print(f'Fibonacci series of {len(FibNum)} numbers is : {output}')