def is_subsequence(s, t):
    left = right = 0

    while left < len(s) and right < len(t):
        if s[left] == t[right]:
            left += 1

        right += 1
    
    return left == len(s)


assert is_subsequence("abc", "ahbgdc") == True
assert is_subsequence("axc", "ahbgdc") == False
assert is_subsequence("", "ahbgdc") == True
assert is_subsequence("b", "abc") == True
