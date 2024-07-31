def runningSum(nums):
    if not nums:
        return []
    
    res = [nums[0]]

    for i in range(len(nums)-1):
        res.append(res[i] + nums[i+1])
    
    return res

print(runningSum([1,2,3,4]))
print(runningSum([1,1,1,1,1]))
print(runningSum([3,1,2,10,1]))
