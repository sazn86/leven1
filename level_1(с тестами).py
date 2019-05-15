b = []
c = []
l = 0
def poisk (a):
    b.append([])
    print (b)
    for i in range(len(a)):
        if len(a[i]) < 2:
            b.append(a[i][0])
        else:
            b.append(a[i][0])
            for k in range(1,len(a[i])):
                c = []
                for j in range(len(a)):
                    c.append([])
                    for m in range(len(a[j])):
                        c[j].append(a[j][m])
                c[i].clear()
                c[i].append((a[i][k]))
                print (c)
                #l = l + 1
                poisk(c)
poisk([[1,2],[3],[5],[6,8]])
print (b)
