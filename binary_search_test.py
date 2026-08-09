def binary_search(arr, target):
    left, right = 0, len(arr)-1
    while left <= right:
        mid = (left + right)//2
        if arr[mid] == target:
            return mid
        left = mid + 1 if arr[mid] < target else right - 1
    return -1

# Test data
arr = [1, 2, 3, 5, 7, 8, 9]
target = 8

print("Array:", arr)
print("Target:", target)
print("Index:", binary_search(arr, target))
