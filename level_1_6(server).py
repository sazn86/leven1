def WordSearch(len1, s, subs):
    x = list(s)
    k = 0
    l = 0
    b = 0
    y = []
    m = []
    for i in range((len(x))):
        y.append([])
        # Определяем длину одного слотка(списка):
        z = 0
        if (l + len1 + 1) <= len(x):
            b = l + len1 + 1
        else:
            b = len(x)
        for j in range(l,(b)):
            if x[j] == ' ':
                k = j
                z = 1
        if z == 0 and l != 0:
            k = k + len1 + 1
        elif z == 0 and l == 0:
            k = k + len1
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
    for i in range((len(y))):
        index =  0
        index = (''.join(y[i]))
        index = index.split()
        index = index.count(subs)
        if index == 0:
            m.append(0)
        else:
            m.append(1)
    return m
