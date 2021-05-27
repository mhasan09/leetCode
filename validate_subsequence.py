a = [5, 1, 22, 25, 6, -1, 8, 10]
sub = [1, 6, -1, 10]

pointer_a = 0
pointer_b = 0
x = len(sub)
for i in range(len(a)-1):

    if a[pointer_a] == sub[pointer_b]:
        pointer_a += 1
        pointer_b += 1
    elif len(sub)-1 == pointer_b:
        print("TRUE")
        break


