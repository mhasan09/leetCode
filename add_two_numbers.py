l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]


l1_rev = l1[::-1]
l2_rev = l2[::-1]
a = ''
b = ''
for i in range(len(l1_rev)):
    a += str(l1_rev[i])


for i in range(len(l2_rev)):
    b += str(l2_rev[i])

a = int(a)
b = int(b)
c = a + b
d = str(c)
e = list(str(d))
e = e[::-1]
print(e)


