def sortedSquares(nums):
    res = []
    abs_min_idx = 0

    for i in range(len(nums)):
        if abs(nums[i]) < abs(nums[abs_min_idx]):
            abs_min_idx = i

    left, right = abs_min_idx, abs_min_idx+1

    while left >= 0 and right <= (len(nums)-1):
        if abs(nums[left]) < abs(nums[right]):
            res.append(nums[left]**2)
            left -= 1
        else:
            res.append(nums[right]**2)
            right += 1

    while left >= 0:
        res.append(nums[left]**2)
        left -= 1

    while right <= (len(nums)-1):
        res.append(nums[right]**2)
        right += 1

    return res

arr = [-4,-1,0,3,10]
print(sortedSquares(arr))

arr = [0,1,2,3,4,5]
print(sortedSquares(arr))

arr = [-4,-3,-2,-1,0]
print(sortedSquares(arr))
