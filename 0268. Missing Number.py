def missingNumber(nums):
    n = len(nums)
    total = n * (n+1) // 2
    
    for num in nums:
        total -= num
    
    return total

nums = [3,0,1]
print(missingNumber(nums))

nums = [0,1]
print(missingNumber(nums))

nums = [9,6,4,2,3,5,7,0,1]
print(missingNumber(nums))

nums = [0]
print(missingNumber(nums))

nums = [1]
print(missingNumber(nums))
