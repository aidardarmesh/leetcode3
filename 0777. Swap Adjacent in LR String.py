def can_transform(start, end):
    i, j = 0, 0
    n, m = len(start), len(end)

    while i < n and j < m:
        while i < n and start[i] == 'X':
            i += 1
        while j < m and end[j] == 'X':
            j += 1

        if (i == n) != (j == m):
            return False
        
        if i == n and j == m:
            return True

        if start[i] != end[j]:
            return False
        
        if start[i] == 'R' and i > j:
            return False

        if start[i] == 'L' and i < j:
            return False
        
        i += 1
        j += 1
    
    while i < n and start[i] == 'X':
        i += 1
    while j < m and end[j] == 'X':
        j += 1
        
    return i == n and j == m

