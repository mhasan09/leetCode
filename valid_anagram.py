def isAnagram(s, t):
    data = {}

    if len(s) != len(t):
        return False

    for i in s:
        if i in data:
            data[i] += 1
        else:
            data[i] = 1
    for i in t:
        if i in data:
            data[i] -= 1
        else:
            return False

    for i in data.values():
        if i != 0:
            return False
    return True


print(isAnagram("anagram", "nagaram"))
