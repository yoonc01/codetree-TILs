import heapq
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

G = [[] for _ in range(n)]

for _ in range(m):
    s, e, cost = map(int, input().split())
    G[s - 1].append((e - 1, cost))
    G[e - 1].append((s - 1, cost))

a, b = map(int, input().split())

heap = []
dist = [sys.maxsize for _ in range(n)]
dist[b - 1] = 0

heapq.heappush(heap, (0, b - 1))

while(heap):
    min_dist, min_idx = heapq.heappop(heap)
    if dist[min_idx] != min_dist:
        continue
    
    for to_idx, to_dist in G[min_idx]:
        new_dist = dist[min_idx] + to_dist
        if dist[to_idx] > new_dist:
            dist[to_idx] = new_dist
            heapq.heappush(heap, (new_dist, to_idx))

print(dist[a - 1])

x = a - 1
print(x + 1, end = " ")
while(x != b - 1):
    G[x].sort()
    for to_idx, to_dist in G[x]:
        if dist[x] == dist[to_idx] + to_dist:
            x = to_idx
            break
    print(x + 1, end = " ")