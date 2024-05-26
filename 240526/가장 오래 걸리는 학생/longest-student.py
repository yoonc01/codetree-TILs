import heapq as hq
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

G = [[] for _ in range(n)]
dist = [sys.maxsize for _ in range(n)]

for _ in range(m):
    s, e, w = map(int, input().split())
    G[s - 1].append((e - 1, w))
    G[e - 1].append((s - 1, w))

dist[n - 1] = 0
heap = []

hq.heappush(heap, (0, n - 1))

while(heap):
    min_dist, min_idx = hq.heappop(heap)

    if (dist[min_idx] != min_dist):
        continue
    
    for to_idx, to_dist in G[min_idx]:
        new_dist = dist[min_idx] + to_dist
        if (new_dist < dist[to_idx]):
            dist[to_idx] = new_dist
            hq.heappush(heap, (new_dist, to_idx))

print(max(dist))