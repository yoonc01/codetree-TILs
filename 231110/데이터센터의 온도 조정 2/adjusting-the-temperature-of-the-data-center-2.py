import sys

input = sys.stdin.readline

n, c, g, h = map(int, input().split())

def work(ta, tb, t):
    if t < ta:
        return c
    elif ta <= t < tb:
        return g
    else:
        return h

info = []
min_val = sys.maxsize
max_val = -sys.maxsize

for _ in range(n):
    a, b = map(int, input().split())
    min_val = min(a, b, min_val)
    max_val = max(a, b, max_val)
    info.append([a, b])

ans = -sys.maxsize
for t in range(min_val - 1, max_val + 2):
    total = 0
    for ta, tb in info:
        total = total + work(ta, tb, t)
    ans = max(ans, total)
print(ans)