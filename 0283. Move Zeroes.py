def moveZeroes(nums):
    last_non_zero_idx = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[last_non_zero_idx], nums[i] = nums[i], nums[last_non_zero_idx]
            last_non_zero_idx += 1
    
    return nums

nums = [0,1,0,3,12]
print(moveZeroes(nums))

nums = [0]
print(moveZeroes(nums))

