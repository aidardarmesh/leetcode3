def binary_search_matrix(matrix, target):
    n, m = len(matrix), len(matrix[0])
    left, right = 0, n * m - 1

    while left <= right:
        mid = (left + right) // 2
        row = mid // m
        col = mid % m
        num = matrix[row][col]

        if num == target:
            return True
        
        if num < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return False