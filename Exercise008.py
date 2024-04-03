'''
An online retailer sells two products: widgets and gizmos. Each widget weighs 75
grams. Each gizmo weighs 112 grams. Write a program that reads the number of
widgets and the number of gizmos in an order from the user. Then your program
should compute and display the total weight of the order.
'''

widgetsNUM = int(input('Number of widgets: '))
gizmosNUM = int(input('Number of gizmos: '))

weight = widgetsNUM * 75 + gizmosNUM * 112

print(f'The total weight of {widgetsNUM} widgets, and {gizmosNUM} gizmos, is {weight}.')