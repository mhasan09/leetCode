def countSmaller(arr):
    out = []
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if arr[i] > arr[j]:
                out.append(arr[j])
            else:
                continue
    return out

print(countSmaller([5, 2, 6, 1]))
