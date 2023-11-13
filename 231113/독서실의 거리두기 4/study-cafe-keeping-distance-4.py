n = int(input())

l = list(map(int, input()))

seats = []
for i in range(n):
    if l[i] == 1:
        seats.append(i)

ans = 0
for i in range(n):
    for j in range(i + 1, n):
        dis = n + 1
        if j == i or i in seats or j in seats:
            continue
        for seat in seats:
            dis = min(dis, abs(seat - j), abs(seat - i), abs(j - i))
        ans = max(ans, dis)
print(ans)