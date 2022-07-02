# from collections import defaultdict
#
# def groupAnagrams(string_list):
#     # if key is not inside then create a list
#     result = defaultdict(list)  # mapping charCount for list of anagrams
#     for s in string_list:
#         count = [0] * 26  # 0 0 0 ... 26
#         for c in s:
#             count[ord(c) - ord('a')] += 1
#         result[tuple(count)].append(s)
#     return result.values()
#
#
# print(groupAnagrams([["eat", "tea", "tan", "ate", "nat", "bat"]]))


def groupAnagrams(str):
    # if key is not inside then create a list
    result = {}
    for s in str:
        key = "".join(sorted(list(s)))  # key = aet,aet,ant,aet,ant,abt...
        if key in result:
            result[key].append(s)  # aet:[eat,tea]...
        else:
            result[key] = [s]  # aet: [eat]

    return [i for i in result.values()]  # [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]


print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
