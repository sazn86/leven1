def ConquestCampaign(N, M, L, battalion):
    pole = []
#Проверка матрецы на 0:
    def proverka(a,b,c):
        for i in range(a):
            for y in range(b):
                if c[i][y] == 0:
                    return
                else:
                    return
#Создаем поле-карту областей и заполняем 0:
    for i in range(N):
        pole.append([])
        for a in range(M):
            pole[i].append(0)
    print (pole)
# Начальные координаты - первые удары
    for i in range(0,(L*2),2):
        pole[battalion[i]][battalion[i+1]] = 1
    print (pole)
    proverka(N,M,pole)
#Добавление к не нулевым значениям +1 (можно закинуть в функцию):
    for i in range(N):
        for y in range(M):
            if pole[i][y] != 0:
                pole[i][y] += 1
    for i in range(N):
        for y in range(M):
            if pole[i][y] >= 2:
                if (y-1) >= 0:
                    pole[i][(y-1)] = 1
                if (y+1) < M:
                    pole[i][(y+1)] = 1
                if (i-1) >= 0:
                    pole[(i-1)][y] = 1
                if (i+1) < N:
                    pole[(i+1)][y] = 1
    print (pole)
ConquestCampaign(3,4,2,[1,1,2,3])
