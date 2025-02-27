n = int(input())

dp = [0 for _ in range(n + 1)]

for i in range(n + 1):
    if i >= 2:
        dp[i] = max(dp[i - 2] + 1, dp[i])
    if i >= 3:
        dp[i] = max(dp[i - 3] + 1, dp[i])

print(dp[n])
