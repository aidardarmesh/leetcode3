def largestUniqueNumber(nums):
    from collections import defaultdict
    
    cnt = defaultdict(int)

    for n in nums:
        cnt[n] += 1
    
    unique = [n for n in cnt if cnt[n] == 1]
    
    if not unique:
        return -1
    
    return max(unique)

print(largestUniqueNumber([5,7,3,9,4,9,8,3,1]))
print(largestUniqueNumber([9,9,8,8]))
