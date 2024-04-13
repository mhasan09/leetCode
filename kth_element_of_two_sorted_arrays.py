def k_th_element(array1, array2, m, n, k):
    p, q, counter = 0, 0, 0
    answer = 0

    while p < m and q < n:
        if counter == k:
            break
        elif array1[p] < array2[q]:
            answer = array1[p]
            p += 1
        else:
            answer = array2[q]
            q += 1
        counter += 1

    if counter != k:
        if p != m - 1:
            answer = array1[k - counter]
        else:
            answer = array2[k - counter]
    return answer


print(k_th_element([1, 3, 5, 7,9,10], [2], 6, 1, 5))
# print(k_th_element([2, 3, 6, 7, 9], [1, 4, 8, 10], 5, 4, 5))
# print(k_th_element([2, 3, 6, 7, 9], [1, 4, 8, 10], 5, 4, 8))
# print(k_th_element([8, 9, 10, 11], [1, 6, 7, 9, 81, 82], 4, 6, 3))
