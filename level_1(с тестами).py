b = []
c = []
z = 0
l = 0
def poisk (a):
    for i in range(len(a)):
        if len(a[i]) < 2:
            return (a[i][0])
            b.append(a[i][0])
        else:
            for k in range(1,len(a[i])):
                c = []
                for j in range(len(a)):
                    for m in range(len(a[j])):
                        c[j].append(a[j][m])
                c[i].clear()
                c[i].append((a[i][k]))
                print (c)
                poisk(c)
poisk([[1,2],[3],[5],[6]])
print (b)
