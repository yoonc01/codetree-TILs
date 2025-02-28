n = int(input())

dp = [0 for _ in range(max(3, n + 1))]

dp[0] = 0
dp[1] = 1
dp[2] = 3

for i in range(3, n + 1):
    dp[i] = (2 * dp[i - 2] + dp[i - 1]) % 10007

print(dp[n])