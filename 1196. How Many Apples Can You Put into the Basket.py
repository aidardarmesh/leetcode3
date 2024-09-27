def max_apples_num(weight):
    import heapq

    ans, limit = 0, 5_000
    heapq.heapify(weight)

    while weight:
        if weight[0] > limit:
            break
        
        ans += 1
        limit -= heapq.heappop(weight)
    
    return ans

