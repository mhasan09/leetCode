def finder_func(mid, n):
    answer = 1
    for i in range(n):
        answer *= mid
    return answer



def nth_root(n: int, m: int) -> int:
    low = 1
    high = m
    while low <= high:
        mid = (low+high)//2
        data = finder_func(mid, n)
        if data > m:
            high = mid - 1
        elif data < m:
            low = mid + 1
        else:
            return mid
    return -1

print(nth_root(3, 27))
print(nth_root(5, 1024))
