import sys

input = sys.stdin.readline

n = int(input())
G = [list(map(int, input().split())) for _ in range(n)]

ans = 0

def in_range(x, y):
    return (0 <= x < n and 0 <= y < n)

def visit(x, y, w, h):
    global ans
    cnt = 0
    dxs = [1, 1, -1, -1]
    dys = [1, -1, -1, 1]
    moveCnt = [w, h, w, h]
    for dx, dy, repeat in zip(dxs, dys, moveCnt):
        for _ in range(repeat):
            x = x + dx
            y = y + dy

            if (not in_range(x, y)):
                return;
            cnt = cnt + G[x][y]
    ans = max(ans, cnt)

for i in range(n):
    for j in range(n):
        for w in range(1, n):
            for h in range(1, n):
                visit(i, j, w, h)

print(ans)