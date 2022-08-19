def square_of_sorted_array(arr):
    square_arr = [arr[i]*arr[i] for i in range(0,len(arr))]
    return sorted(square_arr)

print(square_of_sorted_array([-4, -1, 0, 3, 10]))
print(square_of_sorted_array([-7, -3, 2, 3, 11]))
