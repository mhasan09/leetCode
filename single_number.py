def single_number(arr):
    if len(arr) == 1:
        return arr[0]
    data = {}
    for i in arr:
        if i in data:
            data[i] += 1
        else:
            data[i] = 1
    print(data)
    for i in data:
        if data[i] != 2:
            return i


print(single_number([4, 1, 2, 1, 2]))
print(single_number([1]))
print(single_number([2,2,1]))
