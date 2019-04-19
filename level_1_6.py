def WordSearch(len, s, subs):
    x = list(s)
    k = 0
    y = []
    for i in range(7):
        y.append([])
        for j in range(k,(k+len)):
            if x[j] == ' ':
                k = j
        if x[k] == ' ':
            for a in range((k+1),(k+2+len)):
                y[i].append(x[a])
        else:
            for a in range((k),(k+1+len)):
                y[i].append(x[a])
    print (y)
WordSearch(12, "1) строка разбивается на набор строк через выравнивание по заданной ширине.", "строк")
