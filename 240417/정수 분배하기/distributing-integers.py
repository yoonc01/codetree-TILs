import sys

input = sys.stdin.readline

def cal(l, mid):
    cnt = 0
    for i in l:
        cnt = cnt + i // mid

    return cnt

n, m = map(int, input().split())

l = []

for _ in range(n):
    l.append(int(input().rstrip()))

left = 1
right = min(l)
ans = 0

while(left <= right):
    mid = (left + right) // 2
    if cal(l, mid) >= m:
        left = mid + 1
        if cal(l, mid) == m:
            ans = max(ans, mid)
    elif cal(l, mid) < m:
        right = mid - 1

print(ans)