n = int(input())

dp = [0 for i in range(n + 1)]

dp[0] = 1

for i in range(n + 1):
    if i - 1 >= 0:
        dp[i] = dp[i] + dp[i - 1]
    if i - 2 >= 0:
        dp[i] = dp[i] + dp[i - 2]
    if i - 5 >= 0:
        dp[i] = dp[i] + dp[i - 5]

print(dp[n])