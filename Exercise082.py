'''
In a particular jurisdiction, taxi fares consist of a base fare of $4.00, plus $0.25
for every 140 meters traveled. Write a function that takes the distance traveled (in
kilometers) as its only parameter and returns the total fare as its only result. Write a
main program that demonstrates the function.
'''

def calculateTaxiFare(distanceInKilometers):
    baseFare = 4.00
    costPer140Meters = 0.25
    distanceInMeters = distanceInKilometers * 1000
    additionalFare = (distanceInMeters / 140) * costPer140Meters
    totalFare = baseFare + additionalFare
    return totalFare


distance = float(input("Enter the distance traveled in kilometers: "))
fare = calculateTaxiFare(distance)
print(f"The total taxi fare for {distance} kilometers is: ${fare:.2f}")

