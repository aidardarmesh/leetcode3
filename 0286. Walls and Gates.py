def walls_and_gates(rooms):
    n, m = len(rooms), len(rooms[0])

    from collections import deque

    def bfs(r, c):
        q = deque([(r,c,0)])
        seen = set([(r,c)])

        while q:
            r, c, dist = q.popleft()

            for nr, nc in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
                if 0 <= nr < n and 0 <= nc < m and rooms[nr][nc] != -1 and rooms[nr][nc] != 0 and not (nr,nc) in seen:
                    rooms[nr][nc] = min(rooms[nr][nc], dist+1)
                    q.append((nr,nc,dist+1))
                    seen.add((nr,nc))

    for r in range(n):
        for c in range(m):
            if rooms[r][c] == 0:
                bfs(r, c)

