'''
Maximum Subarray Sum Problem using Dynamic Programming
Given an array of integers (which may include negative numbers), the task is to find the contiguous subarray with the largest sum.

Example 1:

Input: arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

Output: 6

Explanation: The subarray [4, -1, 2, 1] has the maximum sum 4 + (−1) + 2 + 1 = 6

Example 2:

Input: arr = [1, 2, 3, -2, 5]

Output: 9

Explanation: The subarray [1, 2, 3, -2, 5] has the maximum sum 1 + 2 + 3 + (−2) + 5 = 9.
'''

def maxSubarraySum(arr):
    n = len(arr)
    dp = [0] * n
    
    dp[0] = arr[0]
    mamSum = dp[0]
    
    for i in range(1, n):
        dp[i] = max(arr[i], dp[i - 1] + arr[i])
        mamSum = max(mamSum, dp[i])
    
    return mamSum

print(maxSubarraySum([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  
print(maxSubarraySum([1, 2, 3, -2, 5]))                