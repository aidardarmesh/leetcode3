def getAverages(nums, k):
    prefix_sum = [nums[0]]
    avgs = []

    for i in range(1, len(nums)):
        prefix_sum.append(prefix_sum[i-1] + nums[i])
    
    for i in range(len(prefix_sum)):
        if i-k < 0 or i+k >= len(prefix_sum):
            avgs.append(-1)
        else:
            avg = (prefix_sum[i+k] - prefix_sum[i-k] + nums[i-k]) // (2*k + 1)
            avgs.append(avg)
    
    return avgs

nums, k = [7,4,3,9,1,8,5,2,6], 3
print(getAverages(nums, k))

nums, k = [1000], 0
print(getAverages(nums, k))

nums, k = [1000], 1000
print(getAverages(nums, k))
