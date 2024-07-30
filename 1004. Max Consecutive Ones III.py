def longestOnes(nums, k):
    left = ans = zeroes = 0

    for right in range(len(nums)):
        if nums[right] == 0:
            zeroes += 1

        while zeroes > k:
            if nums[left] == 0:
                zeroes -= 1
            left += 1
        
        ans = max(ans, right - left + 1)
    
    return ans



nums, k = [1,1,1,0,0,0,1,1,1,1,0], 2
print(longestOnes(nums, k))

nums, k = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3
print(longestOnes(nums, k))
