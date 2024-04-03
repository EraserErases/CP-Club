'''
Pretend that you have just opened a new savings account that earns 4 percent interest
per year. The interest that you earn is paid at the end of the year, and is added
to the balance of the savings account. Write a program that begins by reading the
amount of money deposited into the account from the user. Then your program should
compute and display the amount in the savings account after 1, 2, and 3 years. Display
each amount so that it is rounded to 2 decimal places.
'''

savings = float(input('Enter the amount you have in savings: '))

year1 = savings * 1.04
year2 = year1 * 1.04
year3 = year2 * 1.04

print(f'With the amount ${"{:.2f}".format(savings)}, after one year you will have ${"{:.2f}".format(year1)}. After two years you will have ${"{:.2f}".format(year2)}, and after three years you will have ${"{:.2f}".format(year3)}.')