import heapq
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

G = [[] for _ in range(n)]

for _ in range(m):
    s, e, c = map(int, input().split())
    G[e - 1].append((s - 1, c))

heap = []
dist = [sys.maxsize] * n

dist[n - 1] = 0

heapq.heappush(heap, (0, n - 1))

while(heap):
    min_dist, min_idx = heapq.heappop(heap)

    if dist[min_idx] != min_dist:
        continue
    
    for to_idx, to_dist in G[min_idx]:
        new_dist = dist[min_idx] + to_dist
        if dist[to_idx] > new_dist:
            dist[to_idx] = new_dist
            heapq.heappush(heap, (new_dist, to_idx))

print(max(dist))