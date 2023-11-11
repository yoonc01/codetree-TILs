import sys

input = sys.stdin.readline

n, k = map(int, input().split())

l = []

for _ in range(n):
    l.append(int(input()))

s = min(l)
r = max(l)
ans = 0
for min_val in range(s, r + 1):
    for max_val in range(min_val, r + 1):
        if max_val - min_val > k:
            break
        cnt = 0
        for elem in l:
            if min_val <= elem <= max_val:
                cnt = cnt + 1
        ans = max(ans, cnt)
print(ans)