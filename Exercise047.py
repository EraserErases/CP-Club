'''
The horoscopes commonly reported in newspapers use the position of the sun at the
time of one"s birth to try and predict the future. This system of astrology divides the
year into twelve zodiac signs, as outline in the table below:
Zodiac sign Date range

Capricorn December 22 to January 19
Aquarius January 20 to February 18
Pisces February 19 to March 20
Aries March 21 to April 19
Taurus April 20 to May 20
Gemini May 21 to June 20
Cancer June 21 to July 22
Leo July 23 to August 22
Virgo August 23 to September 22
Libra September 23 to October 22
Scorpio October 23 to November 21
Sagittarius November 22 to December 21
'''
def getZodiacSign(month, day):
    if (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "Aquarius"
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return "Pisces"
    elif (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "Aries"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "Taurus"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "Gemini"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "Cancer"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "Leo"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "Virgo"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "Libra"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "Scorpio"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return "Sagittarius"
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return "Capricorn"

monthNumber = {
    "january": 1,
    "february": 2,
    "march": 3,
    "april": 4,
    "may": 5,
    "june": 6,
    "july": 7,
    "august": 8,
    "september": 9,
    "october": 10,
    "november": 11,
    "december": 12
}


print("Welcome to the Zodiac Sign Finder!")
month = input("Please enter your birth month: ").lower()
day = int(input("Please enter your birth day (1-31): "))

if day < 1 or day > 31 or month not in monthNumber:
    print("Invalid date entered. Please try again.")
    exit()

month = monthNumber[month]

zodiacSign = getZodiacSign(month, day)
print(f"Your zodiac sign is: {zodiacSign}")

