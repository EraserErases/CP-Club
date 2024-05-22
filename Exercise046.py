'''
The year is divided into four seasons: spring, summer, fall and winter. While the
exact dates that the seasons change vary a little bit from year to year because of the
way that the calendar is constructed, we will use the following dates for this exercise:

Season First day
--------------
Spring March 20
Summer June 21
Fall September 22
Winter December 21

'''

month = input('Enter the Month: ').lower()
day = int(input('Enter the day: '))

if month in ('april', 'may'):
    print('Spring')
elif month in ('july', 'augest'):
    print('Summer')
elif month in ('october', 'november'):
    print('Fall')
elif month in ('january', 'february'):
    print('Winter')

if month == 'march':
    print('Winter') if day < 20 else print('Spring')
elif month == 'june':
    print('Spring') if day < 21 else print('Summer')
elif month == 'september':
    print('Summer') if day < 22 else print('Fall')
elif month == 'December':
    print('Fall') if day < 21 else print('Winter')