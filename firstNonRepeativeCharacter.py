def firstNonRepeatingCharacter(string):
    hashtable = {}
    indexTracker = []
    for i in range(0, len(string)):
        if string[i] in hashtable:
            hashtable[string[i]] += 1
        else:
            hashtable[string[i]] = 1
    print(hashtable)
    for i in hashtable:
        if hashtable[i] == 1:
            indexTracker.append(i)
    for i in range(0, len(string)):
        try:
            if indexTracker[0] == string[i]:
                actualIndex = i
                return actualIndex
        except IndexError:
            return -1
    return -1



print(firstNonRepeatingCharacter('abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxy'))

