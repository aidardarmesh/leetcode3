def maxAreaOfIsland(grid):
    if not grid:
        return 0
    
    m, n = len(grid), len(grid[0])
    seen = set()

    def dfs(r, c, m, n, grid, seen):
        seen.add((r,c))

        area = 1
        for dr, dc in [(r-1,c), (r+1,c), (r,c-1), (r,c+1)]:
            if 0 <= dr < m and 0 <= dc < n:
                if grid[dr][dc] == 1 and not (dr, dc) in seen:
                        area += dfs(dr, dc, m, n, grid, seen)
        
        return area

    max_area = 0
    for r in range(m):
        for c in range(n):
            if grid[r][c] == 1 and not (r,c) in seen:
                max_area = max(max_area, dfs(r, c, m, n, grid, seen))
    
    return max_area

