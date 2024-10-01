def generate_parentheses(n):
    def backtrack(n_open, n_closed):
        if n_closed > n or n_open > n:
            return
        
        if n_closed > n_open:
            return
        
        if n_closed == n:
            ans.append("".join(curr[:]))
            return
        
        curr.append("(")
        backtrack(n_open + 1, n_closed)
        curr.pop()
        
        curr.append(")")
        backtrack(n_open, n_closed + 1)
        curr.pop()
    
    ans, curr = [], []
    backtrack(0, 0)
    
    return ans


assert generate_parentheses(1) == ["()"]
assert generate_parentheses(3) == ["((()))","(()())","(())()","()(())","()()()"]

# TC: O(n * 2^n), multiplied to n because of string generation
# SC: O(n)
