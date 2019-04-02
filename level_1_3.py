N = 3
M = 4
L = 2
K = [1,1, 2,3]
def ConquestCampaign(N, M, L, battalion):
    pole = []
#Создем поле-карту областей и заполняем 1
    for i in range(N):
        pole.append([])
        for a in range(M):
            pole[i].append(1)
    print (pole)
#Начальные координаты первые удары
    for y in range(0,(L*2),2):
        pole[battalion[y]][battalion[y+1]] = 0
    print (pole)
ConquestCampaign(3,4,2,[1,1,2,3])
