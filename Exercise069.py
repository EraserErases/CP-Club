'''
The value of π can be approximated by the following infinite series:

Write a program that displays 15 approximations of π. The first approximation

should make use of only the first term from the infinite series. Each additional approxi-
mation displayed by your program should include one more term in the series, making

it a better approximation of π than any of the approximations displayed previously.
'''
output = 3
x, y, z = 2, 3, 4

for _ in range(15):
    if _ % 2 == 0:
        output += 4 / (x * y * z)
    else:
        output -= 4 / (x * y * z)
    x, y, z = x + 2, y + 2, z + 2

print(output)
    
