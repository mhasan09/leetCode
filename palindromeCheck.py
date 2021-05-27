def isPalindrome(string):
    p = 0
    q = len(string)
    while p < q:
        if string[p] == string[q - 1]:
            p += 1
            q -= 1
        else:
            return False
    return True

print(isPalindrome("abcdefghihgfeddcba"))

