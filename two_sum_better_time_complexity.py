a = [3, 5, -4, 8, 11, 1, -1, 6]
a.sort()
print(a)
target = 10

point_a = 0
sum = 0
point_b = len(a) - 1
for i in range(len(a)-1):
   sum = a[point_a] + a[point_b]
   if sum == target:
        x = (a[point_a],a[point_b])
   elif sum<target:
       point_a+= 1
   elif sum>target:
       point_b-= 1

print(x)

