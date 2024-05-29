'''
February 4, 2013 was the last day that pennies were distributed by the Royal Canadian
Mint. Now that pennies have been phased out retailers must adjust totals so that they
are multiples of 5 cents when they are paid for with cash (credit card and debit card
transactions continue to be charged to the penny). While retailers have some freedom
in how they do this, most choose to round to the closest nickel.
Write a program that reads prices from the user until a blank line is entered.
Display the total cost of all the entered items on one line, followed by the amount
due if the customer pays with cash on a second line. The amount due for a cash
payment should be rounded to the nearest nickel. One way to compute the cash
payment amount is to begin by determining how many pennies would be needed to
pay the total. Then compute the remainder when this number of pennies is divided
by 5. Finally, adjust the total down if the remainder is less than 2.5. Otherwise adjust
the total up.
'''

def roundToNearestNickel(amount):
    pennies = round(amount * 100)
    remainder = pennies % 5

    if remainder < 2.5:
        pennies -= remainder
    else:
        pennies += (5 - remainder)
    
    return pennies / 100


print("Enter the prices of the items one by one. Enter a blank line to finish.")

total = 0.0
while True:
    price = input("Enter the price of the item: ")
    if price == "":
        break
    try:
        price = float(price)
        total += price
    except ValueError:
        print("Invalid input. Please enter a valid price.")

cashTotal = roundToNearestNickel(total)

print(f"Total cost: ${total:.2f}")
print(f"Total amount due if paid with cash: ${cashTotal:.2f}")

