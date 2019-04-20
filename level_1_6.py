def WordSearch(len1, s, subs):
    x = list(s)
    k = 0
    l = 0
    b = 0
    y = []
    for i in range(7):
        y.append([])
        z = 0
        if (l + len1) <= len(x):
            b = l + len1
        else:
            b = len(x)
        # Определяем длину одного слотка(списка):
        for j in range(l,(b)):
            if x[j] == ' ':
                k = j
                z = 1
        if z == 0:
            k = k + len1 + 1
        if k > len(x):
            k = len(x)
        # Вносим значения в слот (список):
        if x[k] == ' ':
            for a in range(l,(k)):
                y[i].append(x[a])
            l = k + 1
        elif x[k+1] == ' ':
            for a in range(l,(k)):
                y[i].append(x[a])
            l = k + 1
        else:
            for a in range(l,(k)):
                y[i].append(x[a])
            l =  k
        print (k)
        print (y)
WordSearch(12, "1) строка разбивается на набор строк через выравниван7ие п заданной ширине.", "строк")
