def findKthLargest(nums, k):
    import heapq

    heapq.heapify(nums)
    
    while len(nums) > k:
        heapq.heappop(nums)
    
    return nums[0]

