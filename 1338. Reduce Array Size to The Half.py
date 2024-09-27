def find_min_set_size(arr):
    from collections import Counter
    import heapq

    n, cnt = len(arr), Counter(arr)
    limit = n // 2
    currently_deleted = 0
    min_set = 0
    heap = []

    for _, q in cnt.items():
        heapq.heappush(heap, -q)

    while heap:
        q = heapq.heappop(heap)
        min_set += 1
        currently_deleted += -q

        if currently_deleted >= limit:
            break
    
    return min_set
