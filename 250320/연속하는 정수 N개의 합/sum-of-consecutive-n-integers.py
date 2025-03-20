import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

sum_val = 0
ans = 0
j = 0
for i in range(n):
    while j < n and sum_val < m:
        sum_val = sum_val + arr[j]
        j = j + 1
    if (sum_val == m):
        ans = ans + 1
    sum_val = sum_val - arr[i]

print(ans)