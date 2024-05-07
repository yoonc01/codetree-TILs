import heapq
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

G = [[] for _ in range(n)]

for _ in range(m):
    s, e, c = map(int, input().split())
    G[s - 1].append((e - 1, c))
    G[e - 1].append((s - 1, c))

s, e = map(int, input().split())

dist = [sys.maxsize for _ in range(n)]
dist[s - 1] = 0
heap = []
heapq.heappush(heap, (0, s - 1))

path = [[s] for _ in range(n)]

while(heap):
    min_dist, min_idx = heapq.heappop(heap)
    if dist[min_idx] != min_dist:
        continue

    for to_idx, cost in G[min_idx]:
        new_dist = dist[min_idx] + cost
        if dist[to_idx] > new_dist:
            dist[to_idx] = new_dist
            path[to_idx] = path[min_idx] + [to_idx + 1]
            heapq.heappush(heap, (new_dist, to_idx))

print(dist[e - 1])
print(" ".join(map(str, path[e - 1])))