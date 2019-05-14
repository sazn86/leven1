b = []
c = []
def poisk (a):
    b.append([])
    for i in range(len(a)):
        if len(a[i]) < 2:
            b.append(a[i][0])
        else:
            b.append()
            for k in range(len(a[i])):
                c = []
                for j in range(len(a)):
                    c.append([])
                    for m in range(len(a[j])):
                        c[j].append(a[j][m])
                c[i].clear()
                c[i].append((a[i][k]))
                print (c)
            poisk(c)
poisk([[1],[2,9],[3],[4]])
