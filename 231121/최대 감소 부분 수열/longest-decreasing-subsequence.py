n = int(input())
l = list(map(int, input().split()))
dp = [1] * n
max_val = 0

for i in range(n):
    for j in range(i):
        if l[j] > l[i]:
            dp[i] = max(dp[i], dp[j] + 1)
    max_val = max(max_val, dp[i])
print(max_val)