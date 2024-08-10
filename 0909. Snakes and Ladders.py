from collections import deque

def snakesAndLadders(board):
    n = len(board)
    cells = [None] * (n**2 + 1)
    columns = [c for c in range(n)]
    label = 1
    for row in range(n-1, -1, -1):
        for col in columns:
            cells[label] = (row, col)
            label += 1
        columns.reverse()
    
    dist = [-1] * (n**2 + 1)
    dist[1] = 0
    queue = deque([1])

    while queue:
        curr = queue.popleft()
        
        for dice_number in range(curr + 1, min(curr + 6, n**2) + 1):
            row, col = cells[dice_number]
            destination = (board[row][col] if board[row][col] != -1 else dice_number)
            if dist[destination] == -1:
                dist[destination] = dist[curr] + 1
                queue.append(destination)
    
    return dist[n**2]

board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
print(snakesAndLadders(board))
