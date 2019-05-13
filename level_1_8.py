def HowManyTimes(s, s_generic):
    x = list(s)
    y = list(s_generic)
    a = []
    b = []
    print(x)
    print(y)
    for i in range(len(x)):
        a.append([])
        for k in range(len(y)):
            if x[i] == y[k]:
                a[i].append(k)
    print(a)
HowManyTimes("123", "1102353")
