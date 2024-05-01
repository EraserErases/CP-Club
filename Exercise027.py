'''
Write a program that computes the body mass index (BMI) of an individual. Your
program should begin by reading a height and weight from the user. Then it should

use one of the following two formulas to compute the BMI before displaying it. If
you read the height in inches and the weight in pounds then body mass index is
computed using the following formula:
'''

height = float(input('Height in meters: '))
weight = float(input('Weight in KG: '))

BMI = weight / (height ** 2)

print(f'Your BMI score is {BMI}')