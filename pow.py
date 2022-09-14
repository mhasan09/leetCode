def my_pow(x, n):
    if n == 0:
        return 1
    elif n < 0:
        return my_pow(1 / x, -n)
    elif n % 2 == 0:
        temp = my_pow(x, n//2)
        return temp * temp
    else:
        return x * my_pow(x, n-1)
