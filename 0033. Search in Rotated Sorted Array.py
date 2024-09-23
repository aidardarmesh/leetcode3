def search_rotate_array(nums, target):
    # create fn to find position of min element
    # problem itself guarantees that min will be only one
    def find_min(nums):
        left, right = 0, len(nums)-1
        ans = -1

        while left <= right:
            mid = (left + right) // 2

            if mid == len(nums)-1 or (mid+1 < len(nums) and nums[mid] < nums[mid+1]):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return ans
    
    # apply bin_search for two parts
    def bin_search(nums, target, left, right):
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return -1
    
    min_pos = find_min(nums)
    ans1 = bin_search(nums, target, 0, max(0, min_pos-1))
    ans2 = bin_search(nums, target, min_pos, len(nums)-1)

    if ans1 != -1:
        return ans1
    
    if ans2 != -1:
        return ans2
    
    return -1
