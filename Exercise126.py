'''
Using the definition of a sublist from Exercise 125, write a function that returns a list
containing every possible sublist of a list. For example, the sublists of [1, 2, 3]

are [], [1], [2], [3], [1, 2], [2, 3] and [1, 2, 3]. Note that your func-
tion will always return a list containing at least the empty list because the empty list

is a sublist of every list. Include a main program that demonstrate your function by
displaying all of the sublists of several different lists.
'''

def allsublist(list):
    output = [[]]
    for _1 in range(len(list)):
        for _2 in range(_1 + 1, len(list) + 1):
            output.append(list[_1 : _2])
    return output

print(allsublist([1, 2, 3]))