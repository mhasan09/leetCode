class MyHashSet:

    def __init__(self):
        self.size = 1000
        self.table = [None] * self.size

    def calculate_key(self, key):
        return key % self.size

    def add(self, key: int) -> None:
        kv = self.calculate_key(key)
        if self.table[kv] is None:
            self.table.append(key)
        else:
            self.table[kv].append(key)
        return

    def remove(self, key: int) -> None:
        kv = self.calculate_key(key)
        if self.table[kv] is not None:
            while key in self.table[kv]:
                self.table[kv].remove(key)
        else:
            return None

    def contains(self, key: int) -> bool:
        kv = self.calculate_key(key)
        if self.table[kv] is not None:
            return key in self.table[kv]
        return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
