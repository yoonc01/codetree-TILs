n = int(input())
dist = list(map(int, input().split()))
cost = list(map(int, input().split()))

min_cost = [cost[0] for _ in range(n)]

for i in range(1, n):
    min_cost[i] = min(min_cost[i - 1], cost[i])

ans = 0
for i in range(n - 1):
    ans = ans + min_cost[i] * dist[i]

print(ans)