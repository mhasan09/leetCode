class Solution:
    def maximumMeetings(self, n, start, end):
        data = sorted(list(zip(start, end)), key=lambda x:x[1])
        current = data[0][1]
        count = 1
        for i in range(n):
            if current < data[i][0]:
                count += 1
                current = data[i][1]
        return count

# print(Solution().maximumMeetings(6, [1, 3, 0, 5, 8, 5], [2, 4, 6, 7, 9, 9]))
# print(Solution().maximumMeetings(3, [0,5,15], [30,10,20]))
# print(Solution().maximumMeetings(2, [7,2], [10,4]))
print(Solution().maximumMeetings(47, [86, 32, 31, 98, 37, 65, 98, 71, 99, 58, 59, 32, 52, 69, 15, 75, 4, 86, 57, 36, 83, 18, 58, 50, 43, 29, 98, 53, 80, 5, 89, 73, 8, 97, 17, 100, 9, 21, 55, 55, 32, 74, 60, 32, 87, 72, 54
],[126, 112, 134, 138, 89, 118, 107, 124, 126, 83, 133, 64, 124, 109, 108, 132, 111, 95, 82, 106, 86, 118, 82, 78, 92, 55, 128, 121, 118, 95, 94, 110, 111, 146, 124, 148, 95, 146, 109, 61, 93, 126, 74, 76, 110, 78, 91
]))

