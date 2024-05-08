'''
The length of a month varies from 28 to 31 days. In this exercise you will create
a program that reads the name of a month from the user as a string. Then your
program should display the number of days in that month. Display “28 or 29 days”
for February so that leap years are addressed.
'''

month = input('Enter a month: ').lower()

months = {
    'january' : '31',
    'feburary' : '28 or 29',
    'march' : '31',
    'april' : '30',
    'may' : '31',
    'june' : '30',
    'july' : '31',
    'augest' : '31',
    'september' : '30',
    'october' : '31',
    'november' : '30',
    'december' : '31'
}

if month in months:
    print(f'The number of days in {month.capitalize()} is {months[month]}. ')
