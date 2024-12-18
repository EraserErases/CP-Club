def inversions(arr):
    n = len(arr)
    count = 0

    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                count += 1

    return count

arr1 = [1, 2, 4, 3]
arr2 = [10, 10, 10, 8]

print(inversions(arr1))
print(inversions(arr2))
