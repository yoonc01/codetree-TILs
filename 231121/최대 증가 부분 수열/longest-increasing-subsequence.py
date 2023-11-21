n = int(input())

l = list(map(int, input().split()))
dp = [1 for i in range(n)]

for i in range(n):
    for j in range(i):
        if l[j] < l[i]:
            dp[i] = max(dp[j] + 1, dp[i])

print(max(dp))