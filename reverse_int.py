def reverse_int(digit):
    result = 0
    bit = 1
    if digit < 0:
        bit = -1
        digit = -digit
    else:
        bit = 1
    while digit:
        result = result * 10 + digit % 10
        digit = digit // 10

    if result > pow(2,31):
        return 0
    else:
        return result * bit


# print(reverse_int(321))
print(reverse_int(-321))
