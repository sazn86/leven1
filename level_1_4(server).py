def SynchronizingTables(N, ids, salary):
    a = sorted(ids)
    b = sorted(salary)
    c = []
    for i in range(N):
        for j in range(N):
            if ids[i] == a[j]:
                c.append(b[j])
    return c
