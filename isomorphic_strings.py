class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return list(map(s.find, s)) == list(map(t.find, t))

    '''
        map takes 2 parameters -> (function, set/list/tuple)
        find returns the first occurrence of the string item 
    
    '''


print(Solution().isIsomorphic("bbbaaaba", "aaabbbba"))
print(Solution().isIsomorphic("egg", "add"))
