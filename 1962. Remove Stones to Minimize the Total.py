def minStoneSum(piles, k):
    import heapq

    piles = [-pile for pile in piles]
    heapq.heapify(piles)

    for _ in range(k):
        pile = -heapq.heappop(piles)
        to_remove = pile // 2
        heapq.heappush(piles, -(pile - to_remove))
    
    return -sum(piles)

piles = [5,4,9], k = 2
print(minStoneSum(piles, k))
