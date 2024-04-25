import sys

input = sys.stdin.readline

n, m = map(int, input().split())

dist = [[sys.maxsize for _ in range(n)] for _ in range(n)]

for _ in range(m):
    s, e, x = map(int, input().split())
    dist[s - 1][e - 1] = min(dist[s - 1][e - 1], x)


for i in range(n):
    dist[i][i] = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

for i in range(n):
    for j in range(n):
        print(dist[i][j] if dist[i][j] != sys.maxsize else -1, end = " ")
    print()