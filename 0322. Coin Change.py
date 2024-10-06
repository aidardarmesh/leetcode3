def coin_change(coins, amount):
    dp = [float('inf')]*(amount+1)
    dp[0] = 0
    
    for target in range(1, amount+1):
        for coin in coins:
            if target >= coin:
                dp[target] = min(dp[target], dp[target-coin]+1)
    
    return dp[amount] if dp[amount] != float('inf') else -1


assert coin_change([1,2,5], 11) == 3
assert coin_change([2], 3) == -1
assert coin_change([1], 0) == 0
