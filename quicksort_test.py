def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

# Test data
arr = [3, 8, 1, 5, 9, 2, 7]

print("Original:", arr)
print("Sorted:", quicksort(arr))
