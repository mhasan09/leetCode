def longestSubstringWithoutDuplication(string):
    hashtable = {}
    longest = [0, 1]
    startIndex = 0
    for i, char in enumerate(string):
        if char in hashtable:
            startIndex = max(startIndex, hashtable[char] + 1)
        if longest[1] - longest[0] < i - startIndex + 1:
            longest = [startIndex, i+1]
        hashtable[char] = i
    return string[longest[0]:longest[1]]


print(longestSubstringWithoutDuplication('clementisacap'))