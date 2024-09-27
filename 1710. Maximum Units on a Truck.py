def max_units(boxTypes, truckSize):
    import heapq
    ans, heap = 0, []

    for boxes, units_per_box in boxTypes:
        heapq.heappush(heap, (-units_per_box, boxes))
    
    while heap:
        units_per_box, boxes = heapq.heappop(heap)
        ans += -units_per_box * min(boxes, truckSize)
        truckSize -= boxes

        if truckSize < 0:
            break
    
    return ans
