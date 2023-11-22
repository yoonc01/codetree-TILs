import sys

n, m = map(int, input().split())
coins = list(map(int, input().split()))

dp = [sys.maxsize for i in range(m + 1)]
dp[0] = 0

for i in range(m + 1):
    for coin in coins:
        if i - coin >= 0: #dp[0] = 0 을 넣었기에 dp[i - coin] != sys.maxsize라는 초기화 유무 검사 필요가 없음
            dp[i] = min(dp[i - coin] + 1, dp[i])

print(dp[m] if dp[m] != sys.maxsize else -1)