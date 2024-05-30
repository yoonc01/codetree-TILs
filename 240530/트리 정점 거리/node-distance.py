from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

G = [[] for _ in range(n)]

def bfs(s, e):
    visited = [False for _ in range(n)]
    visited[s] = True
    q = deque()
    q.append((s, 0))
    while(q):
        x, w = q.popleft()
        for to_idx, to_dist in G[x]:
            if not visited[to_idx]:
                visited[to_idx] = True
                if to_idx == e:
                    return w + to_dist
                q.append((to_idx, w + to_dist))

for _ in range(n - 1):
    s, e, w = map(int, input().split())
    G[s - 1].append((e - 1, w))
    G[e - 1].append((s - 1, w))

for _ in range(m):
    s, e = map(int, input().split())
    print(bfs(s - 1, e - 1))