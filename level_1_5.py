def PatternUnlock(N, hits):
    key = [[6, 1, 9], [5, 2, 8], [4, 3, 7]]
    summa = 0
    for i in range(N):
        for j in range(3):
            for k in range(3):
                if hits[i] == key[j][k]:
                    x1 = j
                    y1 = k
    print (x1,y1)
PatternUnlock(4, [1, 2, 3, 4])
