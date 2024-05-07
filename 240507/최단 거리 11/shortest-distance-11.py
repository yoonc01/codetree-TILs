import sys

input = sys.stdin.readline

n, m = map(int, input().split())

G = [[0 for _ in range(n)] for _ in range(n)]

for _ in range(m):
    s, e, cost = map(int, input().split())
    G[s - 1][e - 1] = cost
    G[e - 1][s - 1] = cost

a, b = map(int, input().split())

dist = [sys.maxsize for _ in range(n)]
visited = [False for _ in range(n)]

dist[b - 1] = 0

for _ in range(n):
    min_val = -1
    for i in range(n):
        if visited[i]:
            continue

        if min_val == -1 or dist[min_val] > dist[i]:
            min_val = i
        
    visited[min_val] = True

    for i in range(n):
        if G[min_val][i] != 0:
            if dist[i] > dist[min_val] + G[min_val][i]:
                dist[i] = dist[min_val] + G[min_val][i]

print(dist[a - 1])

x = a - 1

print(x + 1, end = " ")
while(x != b - 1):
    for i in range(n):
        if G[i][x] == 0:
            continue
        if dist[x] == dist[i] + G[i][x]:
            x = i
            break
    print(x + 1, end = " ")