def ConquestCampaign(N, M, L, battalion):
    pole = []
#Проверка матрецы на 0
    def proverka(a,b,c):
        for i in range(a):
            for y in range(b):
                if c[i][y] == 0:
                    return
#Создаем поле-карту областей и заполняем 1
    for i in range(N):
        pole.append([])
        for a in range(M):
            pole[i].append(0)
    print (pole)
#Начальные координаты - первые удары
    for y in range(0,(L*2),2):
        pole[battalion[y]][battalion[y+1]] = 1
    proverka(N,M,pole)
    print (pole)

ConquestCampaign(3,4,2,[1,1,2,3])
