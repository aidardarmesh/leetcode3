def subsets(nums):
    ans, curr = [], []

    def backtrack(i):
        if i >= len(nums):
            ans.append(curr[:])
            return
        
        curr.append(nums[i])
        backtrack(i+1)

        curr.pop()
        backtrack(i+1)
    
    backtrack(0)

    return ans


assert subsets([0]) == [[0], []]
assert subsets([1, 2, 3]) == [[1, 2, 3], [1, 2], [1, 3], [1], [2, 3], [2], [3], []]
