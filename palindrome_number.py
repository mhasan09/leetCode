def palindrome_number(x):
    x = str(x)
    i = 0
    j = len(x) - 1
    if x[0] == "-":
        return False
    else:
        while i < j:
            if x[i] != x[j]:
                return False
            else:
                i += 1
                j -= 1
        return True


print(palindrome_number(121))
