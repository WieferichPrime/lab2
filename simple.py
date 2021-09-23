def simple(n):
    arr = list(True for i in range(n))
    res = []
    arr[0] = arr[1] = False
    p = 2
    while p**2 < n:
        if arr[p]:
            for i in range(p**2, n):
                if i % p == 0 and arr[i]:
                    arr[i] = False
        p += 1
    for i in range(len(arr)):
        if arr[i]:
            res.append(i)
    return res