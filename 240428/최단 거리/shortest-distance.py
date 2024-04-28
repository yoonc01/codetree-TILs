import sys

input = sys.stdin.readline

n, m = map(int, input().split())

G = [list(map(int, input().split())) for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if G[i][j] != 0 and G[i][k] != 0 and G[k][j] != 0:
                G[i][j] = min(G[i][j], G[i][k] + G[k][j])
            elif G[i][k] != 0 and G[k][j] != 0:
                G[i][j] = G[i][k] + G[k][j]

for _ in range(m):
    a, b = map(int, input().split())
    print(G[a - 1][b - 1])