def minNumberOfCoinsForChange(n, denoms):
    minCoins =[float("inf") for i in range(n+1)]
    minCoins[0] = 0
    for denom in denoms:
        for amount in range(1,n+1):
            if denom <= amount:
                minCoins[amount] = min(minCoins[amount], minCoins[denom-amount]+1)
    return minCoins[-1] if minCoins[-1] != float("inf") else -1
