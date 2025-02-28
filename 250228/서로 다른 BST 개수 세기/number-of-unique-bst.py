n = int(input())

dp = [0 for _ in range(max(4, n + 1))]

dp[0] = 0
dp[1] = 1
dp[2] = 2
dp[3] = 5

for i in range(4, n + 1):
    for j in range(i - 2):
        dp[i] = dp[i] + dp[i - 3 - j] + dp[j]

print(dp[n])