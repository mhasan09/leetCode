import collections

class Solution:
    def minWindow(self, s, t):
        if not t or not s:
            return ""

        dict_t = collections.Counter(t)
        required = len(dict_t)
        l, r = 0, 0
        current_window = 0
        window_counts = {}

        ans = float("inf"), None, None

        while r < len(s):
            character = s[r]
            window_counts[character] = window_counts.get(character, 0) + 1

            # If the frequency of the current character added equals to the desired count in t then increment the formed count by 1.
            if character in dict_t and window_counts[character] == dict_t[character]:
                current_window += 1

            # Try and contract the window till the point where it ceases to be 'desirable'.
            while l <= r and current_window == required:
                character = s[l]
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)
                window_counts[character] -= 1
                if character in dict_t and window_counts[character] < dict_t[character]:
                    current_window -= 1
                l += 1

            r += 1
        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]


print(Solution().minWindow("ADOBECODEBANC", "ABC"))