def smallest_divisor(nums, threshold):
    def find_sum(nums, divisor):
        total_sum = 0
        for num in nums:
            total_sum += math.ceil(num / divisor)
        
        return total_sum
    
    left, right = 1, max(nums)
    ans = -1
    
    while left <= right:
        mid = (left + right) // 2
        total_sum = find_sum(nums, mid)
        
        if total_sum <= threshold:
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
    
    return ans


