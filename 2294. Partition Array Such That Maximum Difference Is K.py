def partition_array(nums, k):
    if not nums:
        return 0

    nums.sort()
    ans, group_min = 1, nums[0]

    for i in range(1, len(nums)):
        if nums[i] - group_min > k:
            ans += 1
            group_min = nums[i]
    
    return ans
