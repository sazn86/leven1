N = 3
M = 4
L = 2
K = [2,2, 3,4]
def ConquestCampaign(N, M, L, K):
    pole = []
#Создем поле-карту областей и заполняем 1
    for i in range(N):
        pole.append([])
        for a in range(M):
            pole[i].append(1)
    print (pole)




ConquestCampaign(3,4,2,[2,2,3,4])
