'''
In the United States, fuel efficiency for vehicles is normally expressed in miles-per-
gallon (MPG). In Canada, fuel efficiency is normally expressed in liters-per-hundred

kilometers (L/100 km). Use your research skills to determine how to convert from
MPG to L/100 km. Then create a program that reads a value from the user in American
units and displays the equivalent fuel efficiency in Canadian units.
'''

american = int(input('Enter the fuel efficiency in MPG: '))

canadian = 235.214583 / american

print(f'{american} MPG is equal to {"{:.2f}".format(canadian)} L/100 km.')

