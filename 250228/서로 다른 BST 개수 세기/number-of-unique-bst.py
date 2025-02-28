n = int(input())

dp = [0 for _ in range(max(4, n + 1))]

dp[0] = 0
dp[1] = 1
dp[2] = 2
dp[3] = 5

for i in range(4, n + 1):
    dp[i] = 2 * d[i - 1]
    for j in range(1, i - 1):
        dp[i] = dp[i] + dp[i - 1 - j] * dp[j]

print(dp[n])