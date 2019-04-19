def WordSearch(len, s, subs):
    x = list(s)
    k = 0
    l = 0
    y = []
    for i in range(7):
        y.append([])
        z = 0
        for j in range(l,(l+len)):
            if x[j] == ' ':
                k = j
                z = 1
        if z == 0:
            k = k + len + 1
        if x[k] == ' ':
            for a in range(l,(k)):
                y[i].append(x[a])
            l = k + 1
        else:
            for a in range(l,(k)):
                y[i].append(x[a])
            l =  k
        print (k)
        print (y)
WordSearch(12, "1) строка разбивается на набор строк через выравнивание по заданной ширине.", "строк")
