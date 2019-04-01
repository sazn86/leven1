N = [10, 1]
def odometer(N):
    k = len(N)
    z = 0
    for i in range(k):
        if i == 0:
            z = N[i] * N[i+1]
        elif i % 2 == 0 and i > 0:
            z = z + N[i] * (N[i+1]-N[i-1])
    print (z)
odometer(N)
