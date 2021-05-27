def nonConstructibleChange(coins):
    coins.sort()
    change = 0
    for i in range(0, len(coins)):
        if coins[i] > change+1:
            return change + 1
        change += coins[i]
    return change+1

print(nonConstructibleChange([5,6,1,1,2,3,4,9]))
