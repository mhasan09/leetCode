import collections


class TimeMap:
    def __init__(self):
        self.data = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        arr = self.data[key]
        if not arr:
            return ''
        l, r = 0, len(arr) - 1
        while l <= r:
            mid = (l + r) // 2
            if arr[mid][0] == timestamp:
                return arr[mid][1]
            elif arr[mid][0] < timestamp:
                l = mid + 1
            else:
                r = mid - 1

        if arr[r][0] > timestamp:
            return ''

        return arr[r][1]


# Your TimeMap object will be instantiated and called as such:
obj = TimeMap()
obj.set("foo", "bar", 1)
param_2 = obj.get("foo", 1)
print(param_2)
