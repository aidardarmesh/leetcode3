def nums_same_consec_diff(n, k):
    def backtrack(num, order):
        if order == n:
            ans.append(num)
            return
        
        last_digit = num % 10
        next_digits = set([last_digit - k, last_digit + k])

        for next_digit in next_digits:
            if 0 <= next_digit < 10:
                backtrack(num * 10 + next_digit, order + 1)
    
    ans = []
    for i in range(1, 10):
        backtrack(i, 1)

    return ans

assert nums_same_consec_diff(2,1) == [10,12,21,23,32,34,43,45,54,56,65,67,78,76,89,87,98]
assert nums_same_consec_diff(3,7) == [181,292,707,818,929]

# TC: O(2^n)
# SC: O(2^n)
