a = [[0,1],[2,5],[3]]
b = [0,0,0]
def cikl(c):
    if (len(a)-c-1) == (len(a) - 1):
        for j in range(len(a[(len(a)-c-1)])):
            b[(len(a)-c-1)] = b[(len(a)-c-1)] + 1
            print (b)
        b[(len(a)-c-1)] = 0
    else:
        for k in range(len(a[(len(a)-c-1)])):
            b[(len(a)-c-1)] = b[(len(a)-c-1)] + 1
            cikl((c-1))
        b[(len(a)-c-1)] = 0
for i in range(len(a)):
    cikl(i)
