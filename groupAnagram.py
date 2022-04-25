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

def groupAnagrams(string_list):
    # if key is not inside then create a list
    result = {}
    for s in string_list:
        key = "".join(sorted(list(s)))  # key = aet,aet,ant,aet,ant,abt...
        if key in result:
            result[key].append(s)  # aet:[eat,tea]...
        else:
            result[key] = [s]  # aet: [eat]

    return [i for i in result.values()]  # [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]


print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
