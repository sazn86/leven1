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
SynchronizingTables (3, [50, 1, 1024], [20000, 100000, 90000])
