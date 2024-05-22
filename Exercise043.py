'''
George Washington
Thomas Jefferson
Abraham Lincoln
Alexander Hamilton
Andrew Jackson
Ulysses S. Grant
Benjamin Franklin
'''

noteFace = {
    1 : 'George Washington',
    2 : 'Thomas Jefferson',
    5 : 'Abraham Lincoln',
    10 : 'Alexander Hamilton',
    20 : 'Andrew Jackson',
    50 : 'Ulysses S. Grant',
    100 : 'Benjamin Franklin'

}

value = int(input('Enter the value of your bill: '))

print(f'The person on your bank note (US) is {noteFace[value]}.') if value in noteFace else print('Not a valid bank note value. ')

