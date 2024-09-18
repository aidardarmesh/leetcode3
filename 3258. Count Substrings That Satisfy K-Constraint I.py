def countKConstraintSubstrings(s: str, k: int) -> int:
    zeroes = ones = ans = 0
    left = 0

    for right in range(len(s)):
        if s[right] == "1":
            ones += 1
        else:
            zeroes += 1
        
        while ones > k and zeroes > k:
            if s[left] == "1":
                ones -= 1
            else:
                zeroes -= 1
            
            left += 1

        ans += right - left + 1
    
    return ans
