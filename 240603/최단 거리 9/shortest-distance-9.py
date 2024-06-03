import heapq as hq
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

G = [[] for _ in range(n + 1)]
dist = [sys.maxsize for _ in range(n + 1)]

for _ in range(m):
    s, e, w = map(int, input().split())
    G[s].append((e, w))
    G[e].append((s, w))

s, e = map(int, input().split())

dist[e] = 0
heap = []
hq.heappush(heap, (e, 0))
path = [0 for _ in range(n + 1)]

while(heap):
    node, min_dist = hq.heappop(heap)

    if dist[node] != min_dist:
        continue
    
    for to_node, to_dist in G[node]:
        new_dist = dist[node] + to_dist
        if (new_dist < dist[to_node]):
            dist[to_node] = new_dist
            path[to_node] = node
            hq.heappush(heap, (to_node, new_dist))

print(dist[s])
x = s
paths = [s]

while (x != e):
    x = path[x]
    paths.append(x)

print(" ".join(map(str, paths)))