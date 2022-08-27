def valid_palindrome(s):
    s = "".join([c.lower() for c in s if c.isalnum()])
    return s == s[::-1]

print(valid_palindrome("race car"))