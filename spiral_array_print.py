a = [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
     [13, 14, 15, 16]]

x = []
sr = 0
er = len(a)-1
sc = 0
ec = len(a[0])-1
while sr<=er and sc<=ec:
    for col in range(sc,ec+1):
        x.append(a[sr][col])
    for row in range(sr+1,er+1):
        x.append(a[row][ec])
    for col in reversed(range(sc,ec)):
        x.append(a[er][col])
    for row in reversed(range(sr+1,er)):
        x.append(a[row][sc])

    sr+=1
    er-=1
    sc+=1
    ec-=1

print(x)





