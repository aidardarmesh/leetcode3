def lengthOfLongestSubstring(s):
    from collections import defaultdict

    ans = left = right = 0
    cnt = defaultdict(int)

    for right in range(len(s)):
        cnt[s[right]] += 1

        while cnt[s[right]] > 1:
            cnt[s[left]] -= 1
            left += 1

        ans = max(ans, right - left + 1)
    
    return ans

print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring("bbbbb"))
print(lengthOfLongestSubstring("pwwkew"))
