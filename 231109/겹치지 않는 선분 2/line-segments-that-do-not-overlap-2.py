import sys

input = sys.stdin.readline

n = int(input())

points = []

for _ in range(n):
    points.append(list(map(int, input().split())))

cnt = 0
for i in range(n):
    x1, y1 = points[i]
    overlap = 0
    for j in range(n):
        x2, y2 = points[j]
        if (x2 - x1) * (y2 - y1) < 0:
            overlap = 1
            break
    if (overlap == 0):
        cnt = cnt + 1
print(cnt)