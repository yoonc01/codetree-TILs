n, m = map(int, input().split())

seq = list(map(int, input().split()))

dp = [-1] * (m + 1)
dp[0] = 1

for a in seq:
    for i in range(m, 0, -1):
        if i - a >= 0 and dp[i - a] != -1:
            dp[i] = 1

print("Yes" if dp[m] != -1 else "No")