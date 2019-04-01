def odometer(N):
    k = len(N)
    z = 0
    for i in range(k):
        if i % 2 == 0:
            z = z + N[i] * N[i+1]
    return z
odometer(N)
