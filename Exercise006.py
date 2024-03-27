'''
The program that you create for this exercise will begin by reading the cost of a meal
ordered at a restaurant from the user. Then your program will compute the tax and
tip for the meal. Use your local tax rate when computing the amount of tax owing.
Compute the tip as 18 percent of the meal amount (without the tax). The output from
your program should include the tax amount, the tip amount, and the grand total for
the meal including both the tax and the tip. Format the output so that all of the values
are displayed using two decimal places.
'''

cost = float(input('Cost of a meal from a resturant. '))

tax = cost * 0.13

tip = cost * 0.18

total = cost + tax + tip

print(f"With the base cost of ${'{:.2f}'.format(cost)}, the tax would be ${'{:.2f}'.format(tax)}, the tip would be ${'{:.2f}'.format(tip)}. The total amount would be ${'{:.2f}'.format(total)}.")