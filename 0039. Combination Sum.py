def combination_sum(candidates, target):
    from collections import Counter

    ans, seen = [], []
    curr = []

    def dfs(reminder):
        if reminder < 0:
            return
        
        if reminder == 0:
            c = Counter(curr)
            if not c in seen:
                ans.append(curr[:])
                seen.append(c)
            return
        
        for num in candidates:
            curr.append(num)
            dfs(reminder-num)
            curr.pop()
    
    dfs(target)
    
    return ans


assert combination_sum([2], 1) == []
assert combination_sum([2,3,5], 8) == [[2,2,2,2],[2,3,3],[3,5]]
assert combination_sum([2,3,6,7], 7) == [[2,2,3],[7]]

