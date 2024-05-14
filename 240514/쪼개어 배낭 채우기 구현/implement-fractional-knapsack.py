import sys

input = sys.stdin.readline

n, m = map(int, input().split())

l = []

for _ in range(n):
    w, v = map(int, input().split())
    l.append((v/w, w, v))

l.sort(reverse = True)

ans = 0
for divided, w, v in l:
    if m - w >= 0:
        ans = ans + v
        m = m - w
    else:
        ans = ans + divided * m
        break

print("%.3lf" %(ans))