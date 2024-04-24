'''
Create a program that determines how quickly an object is traveling when it hits the
ground. The user will enter the height from which the object is dropped in meters (m).
Because the object is dropped its initial speed is 0 m/s. Assume that the acceleration
due to gravity is 9.8 m/s
'''

m = int(input('Height (m): '))

print(f'The speed of the object when it hits the ground is {round((0 + 2 * 9.8 * m) ** 0.5, 2)} m/s.')