from collections import deque
import sys

input = sys.stdin.readline

n = int(input())

l = []

for i in range(n):
    s, e = map(int, input().split())
    l.append((s, 1, i + 1))
    l.append((e, -1, i + 1))

l.sort()

q = deque()
for i in range(1, n + 1):
    q.append(i)

d = {}

for point, v, person in l:
    if v == 1:
        com = q.popleft()
        d[person] = com
    else:
        q.appendleft(d[person])

key_list = list(d.keys())
key_list.sort()

for i in key_list:
    print(d[i], end = " ")