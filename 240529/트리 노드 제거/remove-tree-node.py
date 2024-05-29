from collections import deque
import sys

input = sys.stdin.readline

n = int(input())

parents = list(map(int, input().split()))

delete = int(input())

G = [[] for _ in range(n)]

for child, parent in enumerate(parents):
    if parent == -1:
        start = child
        continue
    elif parent == delete or child == delete:
        continue
    G[parent].append(child)

def bfs(s):
    if s == delete:
        return 0
    cnt = 0
    q = deque()
    q.append(s)
    while(q):
        x = q.popleft()
        is_leaf = True
        for child in G[x]:
            if child == delete:
                continue
            q.append(child)
            is_leaf = False
        if (is_leaf):
            cnt = cnt + 1
    return cnt

print(bfs(start))