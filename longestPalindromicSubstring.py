def longestPalindromicSubstring(string):
    current = [0, 1]
    for i in range(1, len(string)):
        odd = getPalindromeFrom(string, i - 1, i + 1)
        even = getPalindromeFrom(string, i - 1, i)
        longest = max(odd, even, key=lambda x: x[1] - x[0])
        current = max(longest, current,  key=lambda x: x[1] - x[0])

    return string[current[0]:current[1]]


def getPalindromeFrom(string, left, right):
    while left >= 0 and right < len(string):
        if string[left] != string[right]:
            break
        left -= 1
        right += 1

    return [left + 1, right]

print(longestPalindromicSubstring("abaxyzzyxf"))