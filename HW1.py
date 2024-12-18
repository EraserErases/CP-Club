def binarySearch(arr, low, high, x):
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == x:
            return True
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return False

def findCommonElements(A, B, C):
    shortest, l1, l2 = sorted([A, B, C], key=len)
    result = []
    for _ in shortest:
        if binarySearch(l1, 0, len(l1) - 1, _) and binarySearch(l2, 0, len(l2) - 1, _):
            if not result or result[-1] != _: 
                result.append(_)
    return result

A = [1, 5, 10, 20, 30]
B = [5, 13, 15, 20]
C = [5, 20]

print(findCommonElements(A, B, C))  # Output: [5, 20]

A1 = [2, 5, 10, 30]
B1 = [5, 20, 34] 
C1 = [5, 13, 19]

print(findCommonElements(A1, B1, C1)) # Output: [5]