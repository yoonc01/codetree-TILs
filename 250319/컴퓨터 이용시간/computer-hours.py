import heapq
import sys

input = sys.stdin.readline

n = int(input().strip())

heap = list(range(1, n + 1))
heapq.heapify(heap)

l = []

for i in range(n):
    p, q = map(int, input().split())
    l.append((p, 1, i))
    l.append((q, -1, i))

l.sort()
ans = [0] * n
d = [0] * n

for x, v, num in l:
    if v == 1:
        d[num] = heapq.heappop(heap)
        ans[num] = d[num]
    else:
        heapq.heappush(heap, d[num])

print(" ".join(map(str, ans)))
