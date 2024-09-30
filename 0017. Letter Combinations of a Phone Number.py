def letter_combinations(digits):
    if not digits:
        return []
    
    mp = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }

    ans, curr = [], []

    def dfs(i):
        if len(curr) >= len(digits):
            ans.append("".join(curr[:]))
            return
        
        for letter in mp[digits[i]]:
            curr.append(letter)
            dfs(i+1)
            curr.pop()
    
    dfs(0)
    
    return ans


assert letter_combinations("") == []
assert letter_combinations("23") == ["ad","ae","af","bd","be","bf","cd","ce","cf"]
assert letter_combinations("2") == ["a","b","c"]

