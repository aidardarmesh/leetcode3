def maxNumberOfBalloons(text):
    from collections import Counter

    cnt = Counter(text)
    word = {
        'a': 1,
        'b': 1,
        'l': 2,
        'o': 2,
        'n': 1
    }

    res = float('inf')

    for key in word:
        res = min(res, cnt[key] // word[key])
    
    return res

print(maxNumberOfBalloons("nlaebolko"))
print(maxNumberOfBalloons("loonbalxballpoon"))
print(maxNumberOfBalloons("leetcode"))
