def next_greater_element(nums1, nums2):
    mapper = {val: key for key, val in enumerate(nums1)}
    res = [-1] * len(nums1)
    stack = []

    for num in nums2:
        while stack and stack[-1] < num:
            idx = mapper.get(stack.pop())

            if idx != None:
                res[idx] = num
        
        stack.append(num)
    
    return res


assert next_greater_element([4,1,2], [1,3,4,2]) == [-1,3,-1]
assert next_greater_element([2,4], [1,2,3,4]) == [3,-1]
