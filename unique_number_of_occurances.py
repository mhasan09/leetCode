def unique_number(arr):
    data = {}
    for i in range(0, len(arr)):
        if arr[i] in data:
            data[arr[i]] += 1
        else:
            data[arr[i]] = 1

    value = set()

    for i in data:
        value.add(data[i])

    return len(data) == len(value)


print(unique_number([1, 2, 2, 1, 1, 3]))
