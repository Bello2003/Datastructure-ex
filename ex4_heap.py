import heapq

# Min Heap
min_heap = []
heapq.heappush(min_heap, 3)
heapq.heappush(min_heap, 1)
heapq.heappush(min_heap, 5)
print("Min Heap:", min_heap)

# Max Heap (en inversant les valeurs)
max_heap = []
heapq.heappush(max_heap, -3)
heapq.heappush(max_heap, -1)
heapq.heappush(max_heap, -5)
print("Max Heap:", [-x for x in max_heap])
