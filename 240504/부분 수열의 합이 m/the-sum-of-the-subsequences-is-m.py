n, m = map(int, input().split())

l = list(map(int, input().split()))

dp = [m + 1] * (m + 1)
dp[0] = 0

for i in l:
    for j in range(m, 0, -1):
        if j - i >= 0 and dp[j - i] != m + 1:
            dp[j] = min(dp[j], dp[j - i] + 1)

print(dp[m])