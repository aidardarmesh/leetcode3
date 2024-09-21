def binary_search(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif target < nums[mid]:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
    
    return -1 


assert binary_search([-1,0,3,5,9,12], 9) == 4
assert binary_search([-1,0,3,5,9,12], 2) == -1

