import heapq

n = int(input())

heap = list(map(int, input().split()))

heapq.heapify(heap)
ans = 0

while(n > 1):
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    ans = ans + a + b
    heapq.heappush(heap, a + b)
    n = n - 1

print(ans)