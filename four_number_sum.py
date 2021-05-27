a = [7, 6, 4, -1, 1, 2]
target = 16
dictionary = {}
quad = []
for i in range(1, len(a) - 1):
    for j in range(i + 1, len(a) - 1):
        currentSum = a[i] + a[j]
        difference = target - currentSum
        if difference in dictionary:
            for p in dictionary[difference]:
                quad.append(p + [a[i], a[j]])
    for k in range(0, i):
        currentSum = a[i] + a[k]
        if currentSum not in dictionary:
            dictionary[currentSum] = [[a[i]],[a[k]]]
        else:
            dictionary[currentSum].append([a[k], a[i]])
print(quad)
