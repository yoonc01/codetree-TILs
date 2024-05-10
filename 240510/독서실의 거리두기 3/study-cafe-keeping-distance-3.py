n = int(input())
sen = list(map(int, input()))

before = 0
dist = 0

for i in range(n):
    if sen[i] == 1:
        if i - before > dist:
            dist = i - before
            between = (before, i)
        before = i

s, e = between
ans = 0
for i in range(s + 1, e):
    sen[i] = 1
    before = 0
    dist = n
    for j in range(1, n):
        if sen[j] == 1:
            dist = min(dist, j - before)
            before = j
    ans = max(ans, dist)
    sen[i] = 0
print(ans)