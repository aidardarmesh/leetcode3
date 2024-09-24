def longest_subsequence_with_limited_sum(nums, queries):
    nums.sort()
    for i in range(1, len(nums)):
        nums[i] += nums[i-1]
    
    ans = []

    def find_last_smaller(nums, target):
        left, right = 0, len(nums)-1
        ans = -1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] <= target:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return ans
    
    for q in queries:
        ans.append(find_last_smaller(nums, q) + 1)
    
    return ans