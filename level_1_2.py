N = [10, 1, 20, 2, 30, 1]
def odometer(N):
    k = len(N)
    z = 0
    for i in range(k):
        if i % 2 == 0:
            z = z + N[i] * N[i+1]
    print (z)
odometer(N)
