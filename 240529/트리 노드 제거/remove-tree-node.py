from collections import deque
import sys

input = sys.stdin.readline

n = int(input())

parents = list(map(int, input().split()))

node = int(input())

d = set()
d.add(node)

G = [[] for _ in range(n)]

for child, parent in enumerate(parents):
    if parent == -1:
        start = child
        continue
    G[parent].append(child)

visited = [False for _ in range(n)]

parents = [-1 for _ in range(n)]

def bfs(s):
    cnt = 0
    visited[s] = True
    q = deque()
    q.append(s)
    while(q):
        x = q.popleft()
        if x in d:
            for child in G[x]:
                if not visited[child]:
                    visited[child] = True
                    d.add(child)
                    q.append(child)
        else:
            for child in G[x]:
                if not visited[child]:
                    visited[child] = True
                    q.append(child)
                    parents[child] = x
            if len(G[x]) == 0:
                cnt = cnt + 1
    return cnt

print(bfs(start))