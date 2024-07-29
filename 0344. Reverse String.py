def reverse(s):
    i, j = 0, len(s)-1

    while i < j:
        s[i], s[j] = s[j], s[i]
        i += 1
        j -= 1

s = ["h","e","l","l","o"]
print(s)
reverse(s)
print(s)
