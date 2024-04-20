import sys

input = sys.stdin.readline

n, m = map(int, input().split())

G = [[0 for _ in range(n)] for _ in range(n)]

for _ in range(m):
    s, e, v = map(int, input().split())
    G[s - 1][e - 1] = v

visited = [False] * n
dist = [sys.maxsize] * n
dist[0] = 0

for i in range(n):
    min_val = -1

    for j in range(n):
        if visited[j]:
            continue

        if min_val == -1 or dist[min_val] > dist[j]:
            min_val = j
    visited[min_val] = True

    for j in range(n):
        if G[min_val][j] == 0:
            continue
        
        dist[j] = min(dist[j], dist[min_val] + G[min_val][j])
    
for i in range(1, n):
    print(dist[i] if dist[i] != sys.maxsize else -1)