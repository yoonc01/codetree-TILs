import sys

input = sys.stdin.readline

n, m = map(int, input().split())

G = [[0 for _ in range(n)] for _ in range(n)]

for _ in range(m):
    s, e, x = map(int, input().split())
    G[s - 1][e - 1] = x
    G[e - 1][s - 1] = x

s, e = map(int, input().split())

dist = [sys.maxsize for _ in range(n)]
visited = [0 for _ in range(n)]
dist[s - 1] = 0
path = [0 for i in range(n)]

for _ in range(n):
    min_idx = -1
    for i in range(n):
        if visited[i]:
            continue

        if min_idx == -1 or dist[i] < dist[min_idx]:
            min_idx = i
        
    visited[min_idx] = 1

    for i in range(n):
        if G[min_idx][i] != 0 and dist[i] > dist[min_idx] + G[min_idx][i]:
            dist[i] = dist[min_idx] + G[min_idx][i]
            path[i] = min_idx

x = e - 1
vertices = [x + 1]

while x != s - 1:
    x = path[x]
    vertices.append(x + 1)

print(dist[e - 1])
for num in vertices[::-1]:
    print(num, end = " ")