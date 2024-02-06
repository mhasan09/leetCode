class Solution:
    def fractionalknapsack(self, weight, value, n, w):
        weigh_val_index = [value // weight for value, weight in list(zip(value, weight))]
        data = sorted(list(zip(value, weight, weigh_val_index)), key=lambda x: x[2], reverse=True)
        current_weight = 0
        current_val = 0
        remaining_weight = w
        for i in data:
            if remaining_weight < i[1]:
                current_val += remaining_weight * i[2]
            else:
                current_weight += i[1]
                current_val += i[0]
                remaining_weight = w - current_weight

        return current_val


print(Solution().fractionalknapsack([10, 20, 30], [60, 100, 120], 3, 50))
print(Solution().fractionalknapsack([10, 20], [60, 100], 2, 50))
