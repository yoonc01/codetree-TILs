from collections import deque
import sys

input = sys.stdin.readline

def in_range(a, b):
    return 0 <= a < n and 0 <= b < n

ans = 0

def bfs(a, b):
    global ans
    q = deque()
    q.append((a, b, 1))
    dxs = [0, 1, 0, -1]
    dys = [1, 0, -1, 0]

    while(q):
        x, y, cnt = q.popleft()
        ans = max(ans, dp[x][y])
        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy
            
            if in_range(nx, ny) and dp[nx][ny] < cnt + 1 and G[nx][ny] > G[x][y]:
                q.append((nx, ny, cnt + 1))
                dp[nx][ny] = cnt + 1


n = int(input())
G = [list(map(int, input().split())) for _ in range(n)]
dp = [[1 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        bfs(i, j)

print(ans)