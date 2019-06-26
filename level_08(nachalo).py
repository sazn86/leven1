b = [0,0,0]
c = []
z = 0
l = 0
#i = 0
def poisk (a):
    for i in range(len(a)):
        cikl(i,a)
        def cikl(b,a):
            if (len(a)-b-1) == (len(a)- 1):
                for j in range(len(a[(len(a)-b-1)])):
                    b[(len(a)-b-1)] = b[(len(a)-b-1)] + 1
                else:
poisk([[0,1,3],[2,5],[4,6]])
