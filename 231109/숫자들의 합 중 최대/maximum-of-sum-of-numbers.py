x, y = map(int, input().split())

ans = 0
for i in range(x, y + 1):
    l = list(map(int, str(i)))
    ans = max(ans, sum(l))
print(ans)