def find_peak(nums):
    left, right = 0, len(nums) - 1
    ans = -1

    while left <= right:
        mid = (left + right) // 2

        if mid == 0 or (mid - 1 >= 0 and nums[mid] > nums[mid-1]):
            ans = mid
            left = mid + 1
        else:
            right = mid - 1
    
    return ans

assert find_peak([1,2,3,1]) == 2
assert find_peak([1,2,1,3,5,6,4]) == 5