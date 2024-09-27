def find_least_num_of_unique(arr, k):
    import collections, heapq

    c = collections.Counter(arr)
    heap = []
    for key, val in c.items():
        heapq.heappush(heap, (val, key))

    for _ in range(k):
        val, key = heapq.heappop(heap)
        val -= 1
        if val == 0:
            continue
        heapq.heappush(heap, (val, key))
    
    return len(heap)
