'''
The Chinese zodiac assigns animals to years in a 12 year cycle. One 12 year cycle is
shown in the table below. The pattern repeats from there, with 2012 being another
year of the dragon, and 1999 being another year of the hare.

Year Animal
2000 Dragon
2001 Snake
2002 Horse
2003 Sheep
2004 Monkey
2005 Rooster
2006 Dog
2007 Pig
2008 Rat
2009 Ox
2010 Tiger
2011 Hare

Write a program that reads a year from the user and displays the animal associated
with that year. Your program should work correctly for any year greater than or equal
to zero, not just the ones listed in the table.
''' 

def getChineseZodiac(year):
    animals = ["Dragon", "Snake", "Horse", "Sheep", "Monkey", "Rooster", "Dog", "Pig", "Rat", "Ox", "Tiger", "Hare"]
    cycleStartYear = 2000
    cycleLength = 12

    if year < 0:
        return "Invalid year"

    cycleOffSet = (year - cycleStartYear) % cycleLength
    return animals[cycleOffSet]


print("Welcome to the Chinese Zodiac Finder!")
year = int(input("Please enter a year (0 or greater): "))

if year < 0:
    print("Invalid year entered. Please try again.")
    exit()

zodiacAnimal = getChineseZodiac(year)
print(f"The Chinese Zodiac animal for the year {year} is: {zodiacAnimal}")