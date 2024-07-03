'''
Write a program that reads numbers from the user until a blank line is entered. Your
program should display the average of all of the values entered by the user. Then
the program should display all of the below average values, followed by all of the
average values (if any), followed by all of the above average values. An appropriate
label should be displayed before each list of values.
'''

numbers = []

print("Enter numbers (blank line to stop):")

while True:
    user_input = input()
    
    if user_input == "":
        break
    
    number = float(user_input)
    numbers.append(number)

if len(numbers) > 0:
    average = sum(numbers) / len(numbers)

    below_average = [num for num in numbers if num < average]
    average_values = [num for num in numbers if num == average]
    above_average = [num for num in numbers if num > average]

    print(f"\nAverage: {average}")

    print("\nBelow average values:")
    for num in below_average:
        print(num)

    print("\nAverage values:")
    for num in average_values:
        print(num)

    print("\nAbove average values:")
    for num in above_average:
        print(num)
else:
    print("No numbers were entered.")
