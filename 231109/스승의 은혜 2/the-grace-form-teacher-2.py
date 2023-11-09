import sys

input = sys.stdin.readline

n, b = map(int, input().split())

p = [int(input()) for i in range(n)]

p.sort()

total = 0
for i in range(len(p)):
    total = total + p[i]

    if total > b:
        total = total - p[i]//2
        if total > b:
            over = 1
        else:
            over = 0
        break
if over:
    print(i)
else:
    print(i + 1)