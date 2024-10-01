def exist(board, word):
    if not board or not word:
        return False

    n, m = len(board), len(board[0])
    seen = set()

    def backtrack(r, c, i, seen):
        if board[r][c] != word[i]:
            return False
        
        if i == len(word)-1:
            return True
        
        for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
            if 0 <= nr < n and 0 <= nc < m and not (nr, nc) in seen:
                seen.add((nr, nc))
                if backtrack(nr, nc, i+1, seen):
                    return True
                seen.discard((nr, nc))
        
        return False
    
    for r in range(n):
        for c in range(m):
            seen.add((r, c))
            if backtrack(r, c, 0, seen):
                return True
            seen.remove((r, c))
    
    return False


assert exist([["a"]], "a") == True
assert exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED") == True
assert exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE") == True
assert exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB") == False

# TC: O(m * n * 3^L) where L is word's length, 3 ways: 4 directions minus the one we're from
# SC: O(L)
