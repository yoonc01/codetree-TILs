n = int(input())
l = list(map(int, input().split()))
dp = [-1 for i in range(n)]
max_val = 0
dp[0] = 0
for i in range(1, n):
    for j in range(i):
        if l[j] + j >= i and dp[j] != -1:
            dp[i] = max(dp[i], dp[j] + 1)
    max_val = max(max_val, dp[i])
print(max_val)