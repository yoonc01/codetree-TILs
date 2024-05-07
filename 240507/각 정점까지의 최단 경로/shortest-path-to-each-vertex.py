import heapq
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

k = int(input())

G = [[] for _ in range(n)]
dist = [sys.maxsize for _ in range(n)]

for _ in range(m):
    s, e, v = map(int, input().split())
    G[s - 1].append((e - 1, v))
    G[e - 1].append((s - 1, v))

dist[k - 1] = 0
heap = []
heapq.heappush(heap, (0, k - 1))

while (heap):
    min_dist, min_idx = heapq.heappop(heap)
    if min_dist != dist[min_idx]:
        continue
    
    for to_idx, to_dist in G[min_idx]:
        if dist[to_idx] > dist[min_idx] + to_dist:
            dist[to_idx] = dist[min_idx] + to_dist
            heapq.heappush(heap, (dist[to_idx], to_idx))

for i in dist:
    print(i if i != sys.maxsize else -1)