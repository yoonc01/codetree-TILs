def move(a, l):
    return l[a - 1]

n, m = map(int, input().split())

l = list(map(int, input().split()))

ans = 0

for i in range(1, n + 1):
    total = 0
    idx = i
    for _ in range(m):
        total = total + move(idx, l)
        idx = move(idx, l)
    ans = max(ans, total)
print(ans)