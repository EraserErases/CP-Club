'''
Find the largest pair sum in an unsorted array
Given an unsorted of distinct integers, find the largest pair sum in it. For example, the largest pair sum is 74. If there are less than 2 elements, then we need to return -1.

Examples:

Input : arr[] = {12, 34, 10, 6, 40}, Output : 74

Input : arr[] = {10, 10, 10}, Output : 20

Input arr[] = {10}, Output : -1
'''

def linearSearch(arr):
    if len(arr) < 2:
        return -1

    num1 = num2 = 0

    for _ in range(len(arr)):
        if arr[_] > num1:
            num2 = num1
            num1 = arr[_]

    return num1 + num2

list1 = [12, 34, 10, 6, 40]
list2 = [10, 10, 10]
list3 = [10]

print(linearSearch(list1))
print(linearSearch(list2))
print(linearSearch(list3))