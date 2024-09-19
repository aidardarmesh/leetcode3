def daily_temperatures(temps: list[int]) -> list[int]:
    ans = [0] * len(temps)
    stack = []
    n = len(temps)

    for i in range(n):
        while stack and temps[stack[-1]] < temps[i]:
            j = stack.pop()
            ans[j] = i-j
        
        stack.append(i)
    
    return ans

assert daily_temperatures([73,74,75,71,69,72,76,73]) == [1,1,4,2,1,1,0,0]
assert daily_temperatures([30,40,50,60]) == [1,1,1,0]
assert daily_temperatures([30,60,90]) == [1,1,0]
