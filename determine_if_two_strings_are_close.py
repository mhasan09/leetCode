from collections import Counter


def closeStrings(word1: str, word2: str) -> bool:
    if len(word1) != len(word2):
        return False

    c1 = Counter(word1)
    c2 = Counter(word2)

    if c1.keys() == c2.keys() and sorted(c1.values()) == sorted(c2.values()):
        return True
    return False


print(closeStrings("cabbba", "abbccc"))
