'''
New year's day January 1
Canada day July 1
Christmas day December 25
'''

holiday = {
    'January 1' : "New year's day",
    'July 1' : 'Canada day',
    'December 25' : 'Christmas day'

}

date = input('Enter a date (Month than day, i.e April 2): ')

print(f'The holiday is {holiday[date]}.') if date in holiday else print('The date is note a holiday.')