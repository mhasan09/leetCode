def buySellStockII(prices):
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            profit += prices[i] - prices[i - 1]
    return profit


print(buySellStockII([7, 1, 5, 3, 6, 4]))
print(buySellStockII([1, 2, 3, 4, 5]))
