'''
A string is a palindrome if it is identical forward and backward. For example “anna”,
“civic”, “level” and “hannah” are all examples of palindromic words. Write a program
that reads a string from the user and uses a loop to determines whether or not it is a
palindrome. Display the result, including a meaningful output message.
'''

string = input('Enter a string: ')

for _ in range(len(string) // 2):
    if string[_] != string[-1 * (_ + 1)]:
        print('Not a palindrome.')
        exit()
    
print('It is a palindrome!')