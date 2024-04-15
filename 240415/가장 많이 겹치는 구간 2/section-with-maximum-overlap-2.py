import sys

input = sys.stdin.readline

n = int(input())

l = []

for _ in range(n):
    s, e = map(int, input().split())
    l.append([s, 1])
    l.append([e, -1])

l.sort()

over_lap = 0
max_val = 0

for p, v in l:
    over_lap = over_lap + v
    if (over_lap > max_val):
        cnt = 1
        max_val = over_lap
    elif over_lap == max_val:
        cnt = cnt + 1
print(max_val)