# Brute Force Approach

def stockbuysell(prices):
    max_profit = 0
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            current = prices[j] - prices[i]
            if max_profit < current:
                max_profit = current
    return max_profit

print("Brute Force Approach:")
print(stockbuysell([2,1,3,4,5]))

# Optimal Approach

def stockbuysell(prices):
    min_profit = float("inf")
    max_profit = 0
    for price in prices:
        if price < min_profit:
            min_profit = price
        else:
            max_profit = max(max_profit, price - min_profit)
    return max_profit

print("Optimal Approach:")
print(stockbuysell([2,1,3,4,5]))