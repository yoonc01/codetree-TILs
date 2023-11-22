n, m = map(int, input().split())
coins = list(map(int, input().split()))

dp = [m for i in range(m + 1)]
dp[0] = 0

for i in range(m + 1):
    for coin in coins:
        if i - coin >= 0:
            dp[i] = min(dp[i - coin] + 1, dp[i])

print(dp[m])