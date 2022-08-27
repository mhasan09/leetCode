def str_str(haystack, needle):
    if len(needle) == 0:
        return 0
    for i in haystack:
        if needle in haystack:
            return i
    return -1


print(str_str("hello", "ll"))
