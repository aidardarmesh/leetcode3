def permute(nums):
    def backtrack(nums, curr, ans):
        if len(curr) == len(nums):
            ans.append(curr[::])
            return
        
        for num in nums:
            if not num in curr:
                curr.append(num)
                backtrack(nums, curr, ans)
                curr.pop()
    
    ans = []
    backtrack(nums, [], ans)
    return ans


assert permute([1]) == [[1]]
assert permute([0,1]) == [[0,1],[1,0]]
assert permute([1,2,3]) == [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
