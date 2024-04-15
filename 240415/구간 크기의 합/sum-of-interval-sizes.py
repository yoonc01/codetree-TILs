import sys

input = sys.stdin.readline

n = int(input())

l = []

for _ in range(n):
    s, e = map(int, input().split())
    l.append((s, 1))
    l.append((e, -1))

l.sort()

over_lap = 0

ans = 0

for p, v in l:
    if over_lap == 0:
        s = p
    over_lap = over_lap + v
    if over_lap == 0:
        e = p
        ans = ans + e - s
print(ans)