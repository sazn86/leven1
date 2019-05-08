def SumOfThe(N, data):
    for i in range(0,N):
        x = []
        for k in range(0,N):
            x.append((data[k]))
        for k in range(0,N):
            x[i] = 0
        if sum(x) == data[i]:
            print (data[i])
            return (data[i])
SumOfThe(4, [0, 4, -5, 1])
