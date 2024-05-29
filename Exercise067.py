'''
A particular zoo determines the price of admission based on the age of the guest.
Guests 2 years of age and less are admitted without charge. Children between 3 and
12 years of age cost $14.00. Seniors aged 65 years and over cost $18.00. Admission
for all other guests is $23.00.
Create a program that begins by reading the ages of all of the guests in a group
from the user, with one age entered on each line. The user will enter a blank line to
indicate that there are no more guests in the group. Then your program should display
the admission cost for the group with an appropriate message. The cost should be
displayed using two decimal places.
'''

def calculateAdmissionCost(age):
    if age <= 2:
        return 0.00
    elif 3 <= age <= 12:
        return 14.00
    elif age >= 65:
        return 18.00
    else:
        return 23.00


print("Enter the ages of the guests one by one. Enter a blank line to finish.")

totalCost = 0.0

while True:
    ageInput = input("Enter the age of the guest: ")
    if ageInput == "":
        break
    try:
        age = int(ageInput)
        totalCost += calculateAdmissionCost(age)
    except ValueError:
        print("Invalid input. Please enter a valid age.")

print(f"The total admission cost for the group is: ${totalCost:.2f}")

