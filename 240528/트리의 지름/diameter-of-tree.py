import sys

input = sys.stdin.readline

n = int(input())

G = [[] for _ in range(n)]
visited = [False for _ in range(n)]
dist = [0 for _ in range(n)]

for _ in range(n - 1):
    s, e, w = map(int, input().split())
    G[s - 1].append((e - 1, w))
    G[e - 1].append((s - 1, w))
    
order = 0

def dfs(x):
    global order

    for to_idx, to_dist in G[x]:
        if not visited[to_idx]:
            order = order + to_dist
            dist[to_idx] = order
            visited[to_idx] = True
            dfs(to_idx)
            order = order - to_dist

visited[0] = True
dfs(0)
max_val = 0
max_idx = 0
for i, value in enumerate(dist):
    if value > max_val:
        max_val = value
        max_idx = i

visited = [False for _ in range(n)]
dist = [0 for _ in range(n)]
order = 0
visited[max_idx] = True
dfs(max_idx)

for i, value in enumerate(dist):
    if value > max_val:
        max_val = value
        max_idx = i

print(max_val)