class Solution:
    def areAlmostEqual(self, s1: str, s2: str):
        if len(s1) != len(s2):
            return False

        if s1 == s2:
            return True

        differences = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                differences.append((s1[i], s2[i]))

                if len(differences) > 2:
                    return False

        return (len(differences) == 2 and
                differences[0][0] == differences[1][1] and
                differences[0][1] == differences[1][0])


print(Solution().areAlmostEqual("bank", "kanb"))
print(Solution().areAlmostEqual("rust", "rtsu"))
print(Solution().areAlmostEqual("appla", "lppal"))
print(Solution().areAlmostEqual("abcd", "dcba"))
print(Solution().areAlmostEqual("bankb", "kannb"))
