def PatternUnlock(N, hits):
    key = [[6, 1, 9], [5, 2, 8], [4, 3, 7]]
    summa = 0
    for i in range((N-1)):
        for j in range(3):
            for k in range(3):
                if hits[i] == key[j][k]:
                    x1 = j
                    y1 = k
        for j in range(3):
            for k in range(3):
                if hits[(i+1)] == key[j][k]:
                    x2 = j
                    y2 = k
        if (x2 - x1 + y2 -y1) == 1 or (x2 - x1 + y2 -y1) == 1:
            summa = summa + 1
        else:
            summa = summa + 1.41421
    print (x1,y1,x2,y2)
    print (summa)
PatternUnlock(9, [1, 2, 3, 4, 5, 6, 2, 7, 8, 9])
