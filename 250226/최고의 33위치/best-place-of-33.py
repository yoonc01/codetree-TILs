import sys

input = sys.stdin.readline

ans = 0
n = int(input())
G = [list(map(int, input().split())) for _ in range(n)]

def in_range(x, y):
    return (0 <= x < n and 0 <= y < n)

def countMax(x, y):
    global ans
    cnt = 0
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            if in_range(i, j) and G[i][j]:
                cnt = cnt + 1
    ans = max(ans, cnt)

for i in range(n):
    for j in range(n):
        countMax(i, j)

print(ans)
