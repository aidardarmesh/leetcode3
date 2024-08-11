def makeGood(s):
    stack = []

    for i in range(len(s)):
        if stack:
            if stack[-1].lower() == s[i].lower() and stack[-1] != s[i]:
                stack.pop()
                continue
        
        stack.append(s[i])
    
    return ''.join(stack)

s = "leEeetcode"
print(makeGood(s))

s = "abBAcC"
print(makeGood(s))

s = "s"
print(makeGood(s))
