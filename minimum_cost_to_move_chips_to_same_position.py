def minCostToMoveChips(chips):
    even = 0
    odd = 0
    for i in chips:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    print(even,odd)
    return min(odd, even)


print(minCostToMoveChips([5, 4, 3, 4, 2]))
