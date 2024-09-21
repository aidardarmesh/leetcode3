def sqrt(x):
    """
    Find right-most value from 0 to x whose squared value is less than x
    """
    left, right = 0, x
    ans = -1

    while left <= right:
        mid = (left + right) // 2

        # making a probe
        if mid ** 2 <= x:
            ans = mid # probe is valid, save it as potential answer
            left = mid + 1 # don't consider it again and try to focus on larger elements
        else:
            right = mid - 1
    
    return ans
