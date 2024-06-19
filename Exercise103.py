'''
A magic date is a date where the day multiplied by the month is equal to the two digit
year. For example, June 10, 1960 is a magic date because June is the sixth month, and
6 times 10 is 60, which is equal to the two digit year. Write a function that determines
whether or not a date is a magic date. Use your function to create a main program
that finds and displays all of the magic dates in the 20th century. You will probably
find your solution to Exercise 100 helpful when completing this exercise.
'''

def isMagicDate(day, month, year):
    two_digit_year = year % 100
    return day * month == two_digit_year


for year in range(1900, 2000):
    for month in range(1, 13):
        for day in range(1, 32):
            if (month in [1, 3, 5, 7, 8, 10, 12] and day > 31) or \
                (month in [4, 6, 9, 11] and day > 30) or \
                (month == 2 and day > 29) or \
                (month == 2 and day == 29 and not (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))):
                continue
            
            if isMagicDate(day, month, year):
                print(f"{month:02}/{day:02}/{year} is a magic date")
