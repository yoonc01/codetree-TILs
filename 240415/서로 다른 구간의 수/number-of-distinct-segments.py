import sys

input = sys.stdin.readline

n = int(input())

l = []

for _ in range(n):
    s, e = map(int, input().split())
    l.append([s, 1])
    l.append([e, -1])

l.sort()

line = 0
cnt = 0

for point, v in l:
    line = line + v
    if line == 0:
        cnt = cnt + 1
print(cnt)