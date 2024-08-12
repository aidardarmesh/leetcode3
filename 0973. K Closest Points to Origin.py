def kClosest(points, k):
    import heapq

    closest = []

    for x, y in points:
        heapq.heappush(closest, (-(x**2 + y**2), x, y))

        if len(closest) > k:
            heapq.heappop(closest)
    
    return [[pair[1], pair[2]] for pair in closest]

