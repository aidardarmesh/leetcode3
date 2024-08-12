def connectSticks(sticks):
    import heapq

    heapq.heapify(sticks)
    totalCost = 0

    while len(sticks) > 1:
        connectedStick = heapq.heappop(sticks) + heapq.heappop(sticks)
        totalCost += connectedStick
        heapq.heappush(sticks, connectedStick)
    
    return totalCost

