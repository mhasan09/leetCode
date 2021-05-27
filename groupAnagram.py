# def groupAnagrams(words):
#     sortedWords = []
#     index = []
#     for i in words:
#         sortedWords.append("".join(sorted(i)))
#     # sortedWords.sort()
#     print(sortedWords)
#     for i in range(len(words)):
#         index.append(i)
#     index.sort(key=lambda x: sortedWords[x])
#     return index
#
#
# print(groupAnagrams(["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]))
#
# def groupAnagrams(words):
#     sortedWords = ["".join(sorted(i)) for i in words]
#     indices = [i for i in range(len(words))]
#     indices.sort(key=lambda x: sortedWords[x])
#     result = []
#     currentAnagramGroup = []
#     currentAnagram = sortedWords[indices[0]]
#     for i in indices:
#         word = words[i]
#         sortedWord = sortedWords[i]
#         if sortedWord == currentAnagram:
#             currentAnagramGroup.append(word)
#             continue
#         result.append(currentAnagramGroup)
#         currentAnagramGroup = [word]
#         currentAnagram = sortedWords
#     result.append(currentAnagramGroup)
#
#     return result
#
#
# print(groupAnagrams(["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]))

def groupAnagrams(words):
    hashtable = {}
    for i in words:
        sortableWord = "".join(sorted(i))
        if sortableWord in hashtable:
            hashtable[sortableWord].append(i)
        else:
            hashtable[sortableWord] = [i]

    return list(hashtable.values())


print(groupAnagrams(["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]))