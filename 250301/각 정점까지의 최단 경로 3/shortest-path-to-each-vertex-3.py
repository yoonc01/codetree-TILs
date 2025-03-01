import heapq
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

G = [[] for _ in range(n + 1)]

for _ in range(m):
    s, e, w = map(int, input().split())
    G[s].append((e, w))

dists = [sys.maxsize for _ in range(n + 1)]

q = [(1, 0)]
dists[1] = 0

while(q):
    s, dist = heapq.heappop(q)
    
    if dists[s] < dist:
        continue

    for to_go, weight in G[s]:
        new_dist = dist + weight

        if dists[to_go] > new_dist:
            heapq.heappush(q, (to_go, new_dist))
            dists[to_go] = new_dist


for i in range(2, n + 1):
    print(dists[i] if dists[i] != sys.maxsize else -1)