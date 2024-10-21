def find_duplicate(nums):
    for i in range(len(nums)):
        num = nums[i]

        if num != i+1: # num is not at the right place
            if nums[num-1] == num:
                return num
            else:
                nums[i], nums[num-1] = nums[num-1], nums[i]
    print(nums)
    return -1


assert find_duplicate([1,3,4,2,2]) == 2
assert find_duplicate([3,1,3,4,2]) == 3
assert find_duplicate([3,3,3,3,3]) == 3
assert find_duplicate([8,7,1,10,17,15,18,11,16,9,19,12,5,14,3,4,2,13,18,18]) == 18
