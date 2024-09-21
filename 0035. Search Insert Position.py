def search_insert(nums, target):
    left, right = 0, len(nums)-1
    ans = -1

    # find position of first greater than target element
    # if not found -> should be last element
    while left <= right: # accepting left == right case for edge case when nums consists of only one element
        mid = (left + right) // 2

        if nums[mid] >= target:
            ans = mid
            right = mid - 1 # getting rid off mid because we've already considered it
        else:
            left = mid + 1
    
    return ans if ans != -1 else len(nums)

print(search_insert([1,3,5,6], 5))
print(search_insert([1,3,5,6], 2))
print(search_insert([1,3,5,6], 7))
