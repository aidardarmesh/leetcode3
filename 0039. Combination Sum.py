def combination_sum(candidates, target):
    def backtrack(path, start, curr):
        if curr == target:
            ans.append(path[:])
            return
        
        for i in range(start, len(candidates)):
            if curr + candidates[i] <= target:
                path.append(candidates[i])
                backtrack(path, i, curr + candidates[i])
                path.pop()
    
    ans = []
    backtrack([], 0, 0)
    return ans


assert combination_sum([2], 1) == []
assert combination_sum([2,3,5], 8) == [[2,2,2,2],[2,3,3],[3,5]]
assert combination_sum([2,3,6,7], 7) == [[2,2,3],[7]]

