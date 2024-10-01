def total_queens(n):
    def backtrack(row, cols, diags, anti_diags):
        if row == n:
            return 1
        
        count = 0
        for col in range(n):
            diag = row - col
            anti_diag = row + col

            # checking if queen can be attacked
            if col in cols or diag in diags or anti_diag in anti_diags:
                continue
            
            # place queen
            cols.add(col)
            diags.add(diag)
            anti_diags.add(anti_diag)

            count += backtrack(row + 1, cols, diags, anti_diags)

            # remove queen
            cols.remove(col)
            diags.remove(diag)
            anti_diags.remove(anti_diag)
        
        return count

    return backtrack(0, set(), set(), set())


assert total_queens(1) == 1
assert total_queens(4) == 2
