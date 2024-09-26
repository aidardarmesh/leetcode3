def successful_pairs(spells, potions, success):
    def binary_search(potions, target):
        left, right = 0, len(potions)-1
        ans = -1

        while left <= right:
            mid = (left + right) // 2

            if potions[mid] >= target:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return ans if ans != -1 else len(potions)

    potions.sort()
    ans = []
    m = len(potions)

    for spell in spells:
        i = binary_search(potions, success / spell)
        ans.append(m-i)
    
    return ans
