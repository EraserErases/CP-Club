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

def fibnum(n):
    if n in (0, 1, 2):
        return 0 if n == 0 else 1 
    else:
        return (fibnum(n-1) + fibnum(n-2))

def fibseq(rep):
    for _ in range(rep):
        print(fibnum(_), end=' ')

num = 9

fibseq(num)