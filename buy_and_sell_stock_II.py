def buy_and_sell_stock_II(arr):
    profit = 0
    current_difference = 0
    for i in range(0, len(arr) - 1):
        if arr[i] < arr[i + 1]:
            current_difference = arr[i + 1] - arr[i]
            profit += current_difference
    return profit


print(buy_and_sell_stock_II([7, 1, 5, 3, 6, 4]))
# print(buy_and_sell_stock_II([1, 2, 3, 4, 5]))
