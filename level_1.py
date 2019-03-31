def squirrel(N):
    x = 1
    for i in range(1,N+1):
        x = x * i
    while x > 0:
        a = x
        x = x // 10
    return a
