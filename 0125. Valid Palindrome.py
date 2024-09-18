def isPalindrome(s: str) -> bool:
    new_s = []
    for ch in s:
        if ch.isdigit() or ch.isalpha():
            new_s.append(ch.lower())
    s = "".join(new_s)

    left, right = 0, len(s)-1    
    while left < right:
        if s[left] != s[right]:
            return False
        
        left += 1
        right -= 1
    
    return True


print(isPalindrome("amanaplanacanalpanama"))
print(isPalindrome("race a car"))
print(isPalindrome(" "))

