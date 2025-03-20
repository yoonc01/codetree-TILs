import sys

input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

idx_b = 0
ans = "Yes"
for idx_b in range(m):
    idx_a = 0
    while idx_a < n and a[idx_a] != b[idx_b]:
        idx_a = idx_a + 1
    if (idx_a == n):
        ans = "No"
        break
    idx_a = idx_a + 1

print(ans)