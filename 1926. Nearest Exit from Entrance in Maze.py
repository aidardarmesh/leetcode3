def nearestExit(maze, entrance):
    from collections import deque

    queue = deque()
    queue.append((entrance[0], entrance[1], 0))
    m, n = len(maze), len(maze[0])

    seen = set()
    seen.add((entrance[0], entrance[1]))

    while queue:
        r, c, path = queue.popleft()
        for dr, dc in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
            if 0 <= dr < m and 0 <= dc < n and maze[dr][dc] == '.' and not (dr,dc) in seen:
                if dr == 0 or dc == 0 or dr == m-1 or dc == n-1:
                    return path+1
                
                queue.append((dr,dc,path+1))
                seen.add((dr,dc))

    return -1

maze = [["+","+","+"],[".",".","."],["+","+","+"]]
entrance = [1,0]
print(nearestExit(maze, entrance))
