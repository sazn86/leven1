N = int(input("Введите целое не отрицательное число"))
def squirrel(z):
    x = 1
    for i in range(1,z+1):
        x = x * i
    print (x)
    while x > 0:
        a = x
        x = x // 10
    print (a)
squirrel(N)
