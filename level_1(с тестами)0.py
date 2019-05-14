a = [[1,2],[2],[3],[4]]
c = []
for j in range(len(a)):
    c.append([])
    for m in range(len(a[j])):
        c[j].append(a[j][m])
    c[0].clear()
    c[0].append(a[0][0])
print (c)
