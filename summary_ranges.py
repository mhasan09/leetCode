def summaryRanges(arr):
    result = []
    i = 0
    while i < len(arr):
        s = e = i
        while e + 1 < len(arr) and arr[e] + 1 == arr[e + 1]:
            e += 1
        if s == e:
            result.append(f'arr[s]')
        else:
            result.append(f'{arr[s]}->{arr[e]}')
        i = e + 1
    return result


print(summaryRanges([0, 1, 2, 4, 5, 7]))
