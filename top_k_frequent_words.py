from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dictionary = {}
        for i in words:
            dictionary[i] = 1 + dictionary.get(i, 0)

        dictionary = dict(sorted(dictionary.items(), key=lambda x: (-x[1], x[0])))
        print(dictionary)
        return list(dictionary.keys())[:k]


# print(Solution().topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2))
print(Solution().topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 3))
