def is_subset_sum(arr, n, total_sum):
    # Initialize a table to store the results of sub problems
    data = [[False for _ in range(total_sum + 1)] for _ in range(n + 1)]

    # If sum is 0, then answer is true (empty subset)
    # each row first item will be 0
    for i in range(n + 1):
        data[i][0] = True

    # If sum is not 0 and set is empty, then answer is false
    # first row each col will be zero
    for i in range(1, total_sum + 1):
        data[0][i] = False

    # Fill the subset table in bottom-up manner
    for i in range(1, n + 1):
        for j in range(1, total_sum + 1):
            if j < arr[i - 1]:
                data[i][j] = data[i - 1][j]
            else:
                data[i][j] = data[i - 1][j] or data[i - 1][j - arr[i - 1]]

    return data[n][total_sum]


# Driver code to test the above function
arr = [3, 34, 4, 12, 5, 2]
total_sum = 17
n = len(arr)
if is_subset_sum(arr, n, total_sum):
    print("Found a subset with given sum")
else:
    print("No subset with given sum")
