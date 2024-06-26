'''
The greatest common divisor of two positive integers, n and m, is the largest number,
d, which divides evenly into both n and m. There are several algorithms that can be
used to solve this problem, including:
Initialize d to the smaller of m and n.
While d does not evenly divide m or d does not evenly divide n do
Decrease the value of d by 1
Report d as the greatest common divisor of n and m
Write a program that reads two positive integers from the user and uses this algorithm
to determine and report their greatest common divisor.
'''

def findGreatestCommonDivisor(n, m):
    d = min(n, m)
    
    while n % d != 0 or m % d != 0:
        d -= 1
        
    return d


print("Enter two positive integers to find their greatest common divisor.")

n = int(input("Enter the first positive integer: "))
m = int(input("Enter the second positive integer: "))

if n <= 0 or m <= 0:
    print("Both numbers must be positive integers. Please try again.")
    exit()

gcd = findGreatestCommonDivisor(n, m)
print(f"The greatest common divisor of {n} and {m} is: {gcd}")

