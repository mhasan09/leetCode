class Solution:
    def countAndSay(self, n: int):
        rle_data = ['1']
        for i in range(n):
            result = self.calculate_rle(str(rle_data[-1]))
            rle_data.append(result)

        return rle_data[n-1]

    def calculate_rle(self, s: str) -> str:
        if len(s) == 0:
            return ''

        if len(s) == 1:
            return '1' + s
        counter = 1
        rle_data = ''

        p, q = 0, 1
        while q < len(s):
            if s[p] != s[q]:
                rle_data += str(counter)
                rle_data += s[p]
                counter = 1
                p = q
            else:
                counter += 1
            q += 1

        rle_data += str(counter) + s[p]

        return rle_data

print(Solution().countAndSay(4))





