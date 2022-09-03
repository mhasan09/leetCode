def str_str(haystack, needle):
    if len(needle) == 0:
        return 0
    for i in range(len(haystack)):
        if haystack[i:i+len(needle)] == needle:
            return i
    return -1




print(str_str("hello", "ll"))
