def findAndReplacePattern(words, pattern):
    def getPattern(s):
        data = {}
        output = []
        i = 0
        for c in s:
            if c in data:
                output.append(data[c])
            else:
                i += 1
                data[c] = i
                output.append(i)
        return output

    p = getPattern(pattern)
    output = []
    for word in words:
        if getPattern(word) == p:
            output.append(word)
    return output


print(findAndReplacePattern(["abc", "deq", "mee", "aqq", "dkd", "ccc"], "abb"))


