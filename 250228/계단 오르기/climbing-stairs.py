n = int(input())

dp = [0 for _ in range(1001)]
dp[0] = 1
dp[1] = 0
dp[2] = 1
dp[3] = 1

for i in range(4, n + 1):
        dp[i] = (dp[i - 3] + dp[i - 2]) % 100007

print(dp[n])