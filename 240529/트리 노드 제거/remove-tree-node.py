import sys

input = sys.stdin.readline

n = int(input())

parents = list(map(int, input().split()))

node = int(input())

d = set()
parents[node] = -1
d.add(node)

for i in range(n):
    if parents[i] in d:
        d.add(i)
        parents[i] = -1

cnt = 0
for i in parents:
    if i != -1:
        cnt = cnt + 1

print(cnt)