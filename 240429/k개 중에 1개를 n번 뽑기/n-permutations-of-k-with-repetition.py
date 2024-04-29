def backtrack(k, n, l):
    if n == 0:
        print(" ".join(map(str, l)))
        return
    
    for i in range(1, k + 1):
        l.append(i)
        backtrack(k, n - 1, l)
        l.pop()


k, n = map(int, input().split())

backtrack(k, n, [])