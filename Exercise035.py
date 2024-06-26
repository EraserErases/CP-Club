'''
It is commonly said that one human year is equivalent to 7 dog years. However this
simple conversion fails to recognize that dogs reach adulthood in approximately two
years. As a result, some people believe that it is better to count each of the first two
human years as 10.5 dog years, and then count each additional human year as 4 dog
years.
'''

yearsH = float(input('Human years: '))

if yearsH < 0:
    print('Negative')
    exit()
elif yearsH > 2:
    yearsD = (yearsH - 2) * 4 + 10.5
else:
    yearsD = yearsH * 5.25

print(yearsD)