def combination_sum_iii(k, n):
    def backtrack(path_sum, start, order):
        if path_sum == n and order == k:
            ans.append(curr[:])
            return
        
        for i in range(start, end_excluded):
            if path_sum + i <= n and order + 1 <= k:
                curr.append(i)
                backtrack(path_sum + i, i + 1, order + 1)
                curr.pop()
    
    start, end_excluded = 1, 10
    ans, curr = [], []
    backtrack(0, start, 0)

    return ans


assert combination_sum_iii(3, 7) == [[1,2,4]]
assert combination_sum_iii(3, 9) == [[1,2,6],[1,3,5],[2,3,4]]
assert combination_sum_iii(4, 1) == []

# TC: O(k * C(9, k)) where C is number of combinations: 9! / (k! * (9-k)!)
# SC: O(k)
