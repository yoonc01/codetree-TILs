import sys

input = sys.stdin.readline

n = int(input())

G = [list(map(int, input().split())) for _ in range(n)]

dp = [[0 for _ in range(n)] for _ in range(n)]

def init():
    dp[0][n - 1] = G[0][n - 1]

    for i in range(1, n):
        dp[i][n - 1] = dp[i - 1][n - 1] + G[i][n - 1]

    for j in range(n - 2, -1, -1):
        dp[0][j] = dp[0][j + 1] + G[0][j]

init()

for i in range(1, n):
    for j in range(n - 2, -1, -1):
        dp[i][j] = max(dp[i - 1][j], dp[i][j + 1]) + G[i][j]

print(dp[n - 1][0])