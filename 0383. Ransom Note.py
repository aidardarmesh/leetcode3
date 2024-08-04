def canConstruct(ransomNote, magazine):
    from collections import Counter

    rCounter, mCounter = Counter(ransomNote), Counter(magazine)

    for letter in rCounter:
        if not letter in mCounter or rCounter[letter] > mCounter[letter]:
            return False
    
    return True

print(canConstruct("a", "b"))
print(canConstruct("aa", "ab"))
print(canConstruct("aa", "aab"))
