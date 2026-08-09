from app.algorithms import quicksort, binary_search

severity_scores = [3, 8, 2, 5, 9, 1, 7]

print("System Test: QuickSort")
print("Input:", severity_scores)
sorted_scores = quicksort(severity_scores)
print("Sorted:", sorted_scores)

print("\nSystem Test: Binary Search")
lookup_value = 8
print("Lookup Value:", lookup_value)
print("Index Found:", binary_search(sorted_scores, lookup_value))
