import sys

input = sys.stdin.readline

n, m = map(int, input().split())

dp = [[-1 for _ in range(m + 1)] for _ in range(n + 1)]

info = [0]

for i in range(n + 1):
    dp[i][0] = 0

for j in range(m + 1):
    dp[0][j] = 0

for i in range(n):
    info.append(tuple(map(int, input().split())))

ans = 0

for i in range(1, n + 1):
    w, v = info[i]
    for j in range(1, m + 1):
        if j - w >= 0 and dp[i - 1][j - w] != -1:
            dp[i][j] = max(dp[i][j], dp[i - 1][j - w] + v)

        ans = max(ans, dp[i][j])

print(ans)