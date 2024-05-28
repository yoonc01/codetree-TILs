from collections import deque
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

def bfs(s):
    q = deque()
    q.append((s, 0))
    visited[s] = True

    while(q):
        x, w = q.popleft()
        for to_idx, to_dist in G[x]:
            if not visited[to_idx]:
                visited[to_idx] = True
                dist[to_idx] = w + to_dist
                q.append((to_idx, dist[to_idx]))

bfs(0)
max_val = -1
max_idx = -1
for i, v in enumerate(dist):
    if v > max_val:
        max_val = v
        max_idx = i

visited = [False for _ in range(n)]
dist = [0 for _ in range(n)]
bfs(max_idx)
max_val = -1
max_idx = -1
for i, v in enumerate(dist):
    if v > max_val:
        max_val = v
        max_idx = i

print(max_val)