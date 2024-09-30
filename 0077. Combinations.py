def combinations(n, k):
    ans, curr = [], []

    def backtrack(i):
        if len(curr) >= k:
            ans.append(curr[:])
            return
        
        for j in range(i, n+1):
            curr.append(j)
            backtrack(j+1)
            curr.pop()
    
    backtrack(1)

    return ans

