import sys

input = sys.stdin.readline

n, m = map(int, input().split())

list_l = []
for _ in range(m):
    l = list(map(int, input().split()))
    l.sort()
    list_l.append(l)

cnt = 0
ans = 0
for l in list_l:
    cnt = 0
    for j in list_l:
        if l == j:
            cnt = cnt + 1
    ans = max(ans, cnt)
print(ans)