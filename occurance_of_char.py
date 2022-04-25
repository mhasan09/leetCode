string = 'we are are not are'
string = string.split()
d = {}
for i in string:
    if i in d:
        d[i] += 1
    else:
        d[i] = 0
print(d)
max_val = None
max_key = 0
for i in d:
    if max_val is None or max_val < d[i]:
        max_val = d[i]
        max_key = i
print(max_val)
print(max_key)

