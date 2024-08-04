def numJewelsInStones(jewels, stones):
    from collections import Counter

    sCounter = Counter(stones)

    ans = 0
    for j in jewels:
        ans += sCounter[j]
    
    return ans

print(numJewelsInStones("aA", "aAAbbbb"))
print(numJewelsInStones("z", "ZZ"))
