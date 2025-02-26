import sys

input = sys.stdin.readline

n, m = map(int, input().split())
G = [list(map(int, input().split())) for _ in range(n)]
ans = 0

for i in range(n):
    cnt = 1
    pivot = G[i][0]
    for j in range(1, n):
        if G[i][j] == pivot:
            cnt = cnt + 1
        else:
            cnt = 1
            pivot = G[i][j]
        if (cnt == m):
            break
    if (cnt == m):
        ans = ans + 1

for i in range(n):
    cnt = 1
    pivot = G[0][i]
    for j in range(1, n):
        if G[j][i] == pivot:
            cnt = cnt + 1
        else:
            cnt = 1
            pivot = G[j][i]
        if (cnt == m):
            break
    if cnt == m:
        ans = ans + 1

print(ans)