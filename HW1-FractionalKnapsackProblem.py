'''
Scenario:

You're a treasure hunter who's stumbled upon a knapsack filled with valuable items. Each item has a weight and a corresponding value. However, your knapsack has a weight limit, and you want to maximize the total value of the items you carry away.

Challenge:

Write a function fractional_knapsack(capacity, items) that takes the knapsack's capacity (maximum weight) and a list of items as input. Each item is represented as a tuple (weight, value). The function should return the maximum total value you can obtain by taking fractions of items if necessary.

Example:

capacity = 50
items = [(10, 60), (20, 100), (30, 120)] # (weight, value)
fractional_knapsack(capacity, items) # Output: 240
'''

def fractional_knapsack(capacity, items):
    items = sorted(items, key=lambda x: x[1] / x[0], reverse=True)
    total_value = 0    
    for weight, value in items:
        if capacity == 0:
            break 
        if weight <= capacity:
            total_value += value
            capacity -= weight
        else:
            fraction = capacity / weight
            total_value += value * fraction
            capacity = 0 
    return total_value


capacity = 50
items = [(10, 60), (20, 100), (30, 120)]
result = fractional_knapsack(capacity, items)
print(f"Maximum total value: {result}")
