def rob(nums):
    n = len(nums)
        
    if n == 1:
        return nums[0]
    
    dp = [0] * n
    dp[0], dp[1] = nums[0], max(nums[0], nums[1])

    for i in range(2, n):
        dp[i] = max(dp[i-1], dp[i-2] + nums[i])
    
    return dp[-1]


assert rob([1,2,3,1]) == 4
assert rob([2,7,9,3,1]) == 12

# TC: O(n)
# SC: O(n)
