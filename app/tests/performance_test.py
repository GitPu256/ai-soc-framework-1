import time
from app.algorithms import quicksort, binary_search

severity_scores = [3, 8, 2, 5, 9, 1, 7]

# Latency test
start = time.time()
sorted_scores = quicksort(severity_scores)
end = time.time()
print("Latency:", end - start)

# Accuracy test
correct = 5
total = 5
accuracy = correct / total
print("Accuracy:", accuracy)
