def ConquestCampaign(N, M, L, battalion):
    pole = []
    schetchik = 1
#Проверка матрецы на 0:
    def proverka(a,b,c):
        for i in range(a):
            for y in range(b):
                if c[i][y] == 0:
                    return 1
        return 0
#Фенкция прибавление единички к не нулевым значениям
    def plus_1(a,b,c):
        for i in range(a):
            for y in range(b):
                if c[i][y] != 0:
                    c[i][y] += 1
#Создаем поле-карту областей и заполняем 0:
    for i in range(N):
        pole.append([])
        for a in range(M):
            pole[i].append(0)
# Начальные координаты - первые удары
    for i in range(0,(L*2),2):
        pole[(battalion[i]-1)][(battalion[i+1]-1)] = 1
# Распределение десанта:
    for k in range(N*M):
        if  proverka(N,M,pole) == 0:
            break
        plus_1(N,M,pole)
        schetchik += 1
        for i in range(N):
            for y in range(M):
                if pole[i][y] >= 2:
                    if (y-1) >= 0 and pole[i][(y-1)] == 0:
                        pole[i][(y-1)] = 1
                    if (y+1) < M and pole[i][(y+1)] == 0:
                        pole[i][(y+1)] = 1
                    if (i-1) >= 0 and pole[(i-1)][y] == 0:
                        pole[(i-1)][y] = 1
                    if (i+1) < N and pole[(i+1)][y] == 0:
                        pole[(i+1)][y] = 1
    return (schetchik)
