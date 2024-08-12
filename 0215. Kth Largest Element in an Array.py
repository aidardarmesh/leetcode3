def findKthLargest(nums, k):
    import heapq

    nums = [-num for num in nums]
    heapq.heapify(nums)
    
    for _ in range(k-1):
        heapq.heappop(nums)

    return -nums[0]
