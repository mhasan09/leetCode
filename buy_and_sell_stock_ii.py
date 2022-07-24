def stock(prices):
    if not prices or len(prices) == 1:
        return 0

    profit = 0

    for i in range(1, len(prices)):
        # print(prices[i])
        print(prices[i-1])
        if prices[i] > prices[i - 1]:
            profit += prices[i] - prices[i - 1]

    return profit


print(stock([7, 1, 5, 3, 6, 4]))
