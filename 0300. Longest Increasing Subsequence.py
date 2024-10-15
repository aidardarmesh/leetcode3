def lis_max_len(nums):
    dp = [1] * len(nums)
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)


assert lis_max_len([10,9,2,5,3,7,101,18]) == 4
assert lis_max_len([0,1,0,3,2,3]) == 4
assert lis_max_len([7,7,7,7,7,7,7]) == 1
