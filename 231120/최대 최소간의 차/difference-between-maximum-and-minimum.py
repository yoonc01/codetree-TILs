import sys

input = sys.stdin.readline

n, k = map(int, input().split())
l = list(map(int, input().split()))

ans = sys.maxsize

for min_val in range(min(l), max(l) + 1):
    cost = 0
    for i in l:
        if min_val <= i <= min_val + 2:
            continue
        elif i < min_val:
            cost = cost + min_val - i
        else:
            cost = cost + i - min_val - 2
    ans = min(cost, ans)
print(ans)