def plus_one(arr):
    strr = "".join(str(x) for x in arr)
    strr = int(strr)
    strr = strr + 1
    str(strr)
    return [int(i) for i in str(strr)]

def plus_one2(arr):
    if arr[len(arr)-1] != 9:
        arr[len(arr) - 1] += 1
        return arr
    else:
        arr[len(arr)-1] = 0
        arr[:len(arr)-1] = plus_one2(arr[:len(arr)-1])
        return arr


print(plus_one([1, 2, 3]))
print(plus_one([9, 9]))
print(plus_one([3, 1, 9]))
print(plus_one([9]))
