a, b, c = map(int, input().split())

ans = 0
for i in range(c + 1):
    if a * i > c:
        break
    for j in range(c + 1):
        total = a * i + b * j
        if total <= c:
            ans = max(ans, total)
        else:
            break

print(ans)