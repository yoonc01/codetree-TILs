import sys

input = sys.stdin.readline

n = int(input())
G = [list(map(int, input().split())) for _ in range(n)]

dp = [[0 for _ in range(n)] for _ in range(n)]
dp[0][0] = G[0][0]

for i in range(1, n):
    dp[i][0] = dp[i - 1][0] + G[i][0]

for j in range(1, n):
    dp[0][j] = dp[0][j - 1] + G[0][j]

for i in range(1, n):
    for j in range(1, n):
        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + G[i][j]

print(dp[n - 1][n - 1])