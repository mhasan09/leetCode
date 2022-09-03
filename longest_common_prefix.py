def longest_common_prefix(strs):
    str1 = min(strs)
    str2 = max(strs)
    i = 0
    while i < len(str1):
        if str1[i] != str2[i]:
            str1 = str1[:i]
        i += 1
    return str1

# print(longest_common_prefix(["flower", "flow", "flight"]))
print(longest_common_prefix(["flower", "flow", "flowchart"]))
