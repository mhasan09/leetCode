def first_unique(s):
    data = {}
    for i in s:
        if i in data:
            data[i] += 1
        else:
            data[i] = 1

    if 1 not in data.values():
        return -1

    for i in data:
        if data[i] == 1:
            return s.find(i)

print(first_unique("loveleetcode"))
print(first_unique("aabb"))