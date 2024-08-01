def minStartValue(nums):
    min_sum_boundary = 1
    min_positive_num = 1
    prefix_sum = [nums[0]]

    for i in range(1, len(nums)):
        prefix_sum.append(prefix_sum[i-1] + nums[i])
    
    min_start_value = -10_000
    for i in range(len(prefix_sum)):
        min_start_value = max(min_start_value, 1 - prefix_sum[i], min_positive_num)
    
    return min_start_value


nums = [-3,2,-3,4,2] # 5
print(minStartValue(nums))

nums = [1,2] # 1
print(minStartValue(nums))

nums = [3,4] # 1
print(minStartValue(nums))

nums = [7] # 1
print(minStartValue(nums))
