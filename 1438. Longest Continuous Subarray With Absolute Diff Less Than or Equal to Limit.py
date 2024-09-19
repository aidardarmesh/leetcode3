def longest_subarray(nums: list[int], limit: int) -> int:
    from collections import deque

    inc, dec = deque(), deque()
    left = ans = 0

    for right in range(len(nums)):
        while inc and inc[-1] > nums[right]:
            inc.pop()
        while dec and dec[-1] < nums[right]:
            dec.pop()
        
        inc.append(nums[right])
        dec.append(nums[right])

        while dec[0] - inc[0] > limit:
            if nums[left] == dec[0]:
                dec.popleft()
            if nums[left] == inc[0]:
                inc.popleft()
            left += 1
        
        ans = max(ans, right - left + 1)
    
    return ans


assert longest_subarray([8,2,4,7], 4) == 2
assert longest_subarray([10,1,2,4,7,2], 5) == 4
assert longest_subarray([4,2,2,2,4,4,2,2], 0) == 3

