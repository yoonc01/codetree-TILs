n = int(input())

G = [[0 for _ in range(n)] for _ in range(n)]

for j in range(n):
    if (j % 2 == 0):    
        for i in range(n):
            G[i][j] = i + 1
    else:
        for i in range(n):
            G[i][j] = n - i

for i in range(n):
    for j in range(n):
        print(G[i][j], end = '')
    print()
