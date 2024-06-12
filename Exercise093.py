'''
In this exercise you will create a function named nextPrime that finds and returns
the first prime number larger than some integer, n. The value of n will be passed to
the function as its only parameter. Include a main program that reads an integer from
the user and displays the first prime number larger than the entered value. Import
and use your solution to Exercise 92 while completing this exercise.
'''

def isPrime(num):
    for _ in range(int(num ** .5) - 1):
        if num % (_ + 2) == 0:
            return False
    return True

def nextPrime(num):
    num += 2
    while True:
        if isPrime(num) == False:
            num += 2
        else:
            return num


n = int(input('Enter a number: '))

if n % 2 == 0:
    n += 1

print(f'The next prime is {nextPrime(n)}')