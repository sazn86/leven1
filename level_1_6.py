def WordSearch(len1, s, subs):
    x = list(s)
    k = 0
    l = 0
    b = 0
    y = []
    for i in range((len(x))):
        y.append([])
        # Определяем длину одного слотка(списка):
        z = 0
        if (l + len1) <= len(x):
            b = l + len1
        else:
            b = len(x)
        for j in range(l,(b)):
            if x[j] == ' ':
                k = j
                z = 1
        if z == 0:
            k = k + len1 + 1
        # Вносим значения в слот (список):
        if k < len(x):
            for a in range(l,(k)):
                y[i].append(x[a])
            if x[k] == ' ':
                l = k + 1
            else:
                l = k
        else:
            k = len(x)
            for a in range(l,(k)):
                y[i].append(x[a])
            break
    #for i in range(len(y)):
        #for j in range((len(y[i]))
    print (y)
WordSearch(12, "1) строка разбивается на набор строк через выравнивание по заданной ширине.", "строк")
