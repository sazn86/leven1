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
        if (x2 - x1 + y2 -y1) == 1 or (x2 - x1 + y2 -y1) == -1:
            summa = summa + 1
        else:
            summa = summa + 1.41421
    summa = int(summa * 100000)
    summa = str(summa)
    sum2 = summa.replace("0", "")
    return (sum2)
