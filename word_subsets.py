from collections import Counter


def word_subsets(A, B):
    s = set(A)
    totalword = {}
    for b in B:
        temp = Counter(b)
        for k, v in temp.items():
            if k not in totalword:
                totalword[k] = v
            else:
                totalword[k] = max(v, totalword[k])
    for i in A:
        for j in totalword:
            if i.count(j) < totalword[j]:
                s.remove(i)
                break
    return list(s)


print(word_subsets(["amazon", "apple", "facebook", "google", "leetcode"], ["e", "o"]))
