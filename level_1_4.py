def SynchronizingTables(N, ids, salary):
    a = sorted(ids)
    b = sorted(salary)
    c = []
    print (a) #[3, 12, 90]
    print (b) # [25000, 34500, 80000]
    for i in range(N):
        for j in range(N):
            if ids[i] == a[j]:
                c.append(b[j])
    print (c)
SynchronizingTables (10, [1, 3, 243, 234, 4, 5, 6, 9, 121, 123], [21533,20000, 100000, 90000, 123123, 54455, 44464, 5455, 33333, 3434])
