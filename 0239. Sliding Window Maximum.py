def max_sliding_window(nums: list[int], k: int) -> list[int]:
    from collections import deque

    ans, queue = [], deque()

    for i in range(len(nums)):
        # maintain monotonic decreasing
        # all elements smaller than the current one should be removed
        while queue and nums[queue[-1]] < nums[i]:
            queue.pop()
        
        queue.append(i)

        # queue[0] is the index of max element
        # if queue[0] + k == i then max element is out of range
        if queue[0] + k == i:
            queue.popleft()
        
        # only add to the answer once our window has reached size k
        if i >= k-1:
            ans.append(nums[queue[0]])
    
    return ans


assert max_sliding_window([1,3,-1,-3,5,3,6,7], 3) == [3,3,5,5,6,7]
assert max_sliding_window([1], 1) == [1]
